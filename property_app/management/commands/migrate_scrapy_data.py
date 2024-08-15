import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from property_app.models import Property, Image, Location, Amenity
from sqlalchemy import create_engine, Column, Integer, String, Float, ARRAY, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from django.conf import settings
from dotenv import load_dotenv

# Load the .env file from the project
load_dotenv()

Base = declarative_base()
metadata = MetaData()

# Define the table structure of your existing database
hotels = Table('hotels', metadata,
    Column('id', Integer, primary_key=True),
    Column('propertyTitle', String),
    Column('rating', String),
    Column('location', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('room_type', ARRAY(String)),
    Column('img', String)
)


class Command(BaseCommand):
    help = 'Migrate data from existing PostgreSQL database for Scrapy to Django'

    def handle(self, *args, **options):
        # Connect to the existing PostgreSQL database
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            self.stdout.write(self.style.ERROR('DATABASE_URL is not set in .env file'))
            return

        engine = create_engine(database_url)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Path to your local image directory
        LOCAL_IMAGE_DIR = os.path.join(settings.BASE_DIR, '../../web_scraping/trip_scraper/images/full/')

        # Fetch all hotels from the existing database
        result = session.execute(hotels.select())

        # Migrate data to Django
        for row in result:
            # Create or update Property
            property, created = Property.objects.update_or_create(
                title=row.propertyTitle,
                defaults={
                    'rating': row.rating,
                }
            )

            # Create or update Location
            location, _ = Location.objects.get_or_create(
                name=row.location,
                defaults={
                    'type': 'city',  # Assuming all locations are cities
                    'latitude': row.latitude,
                    'longitude': row.longitude,
                }
            )
            property.locations.add(location)

            # Create or update Amenities
            for amenity_name in row.room_type:
                amenity, _ = Amenity.objects.get_or_create(name=amenity_name)
                property.amenities.add(amenity)

            # Check if the image already exists before saving
            if row.img:
                local_img_path = os.path.join(LOCAL_IMAGE_DIR, os.path.basename(row.img))
                
                if os.path.exists(local_img_path):
                    # Check if the image already exists in the database
                    if not Image.objects.filter(property=property, 
                                                image=f'property_images/{property.property_id}/{os.path.basename(row.img)}').exists():
                        with open(local_img_path, 'rb') as img_file:
                            img_temp = NamedTemporaryFile(delete=True)
                            img_temp.write(img_file.read())
                            img_temp.flush()

                            filename = os.path.basename(row.img)
                            if not filename:
                                filename = 'image.jpg'  # Default filename if not present in URL

                            image = Image(property=property)
                            image.image.save(filename, File(img_temp), save=True)
                    else:
                        self.stdout.write(self.style.WARNING(f'Image already exists for 
                                                             property {property.title}: {local_img_path}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Image not found for 
                                                         property {property.title}: {local_img_path}'))


        self.stdout.write(self.style.SUCCESS('Successfully migrated data from existing PostgreSQL database for Scrapy to Django'))

        # Close the SQLAlchemy session
        session.close()     