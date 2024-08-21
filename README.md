# Property Management System

This Django project is a property management application designed to manage and display property listings, locations, amenities, and associated images. The project integrates with an existing PostgreSQL database (the database containing hotel data that were scrped from trip.com using scrapy spider) using both Django ORM and SQLAlchemy to migrate and manage data. The admin interface has been customized to provide a user-friendly management experience for administrators, enabling them to manage properties, images, locations, and amenities seamlessly.


## Features

  1. **Property Management**: Manage properties with details such as ID, title, rating, locations, and amenities. Supports image uploads and previews.
  
  2. **Custom Admin Interface**: Customizations include inline image previews, list filters, search fields, and associations between properties, locations, and amenities.
  
  3. **Data Migration**: Migrate data from an existing PostgreSQL database using a custom management command with SQLAlchemy integration.
  
  4. **Environment Configuration**: Uses a `.env` file for managing sensitive data and project configurations.
  
  5. **Data Integrity**: Enforces unique constraints and supports optional fields in models for flexibility.
  
  6. **Development Best Practices**: Modular code structure and detailed documentation ensure maintainability and ease of use.



## Installation

### Prerequisites

- Python 3.7 or later
- Django
- PostgreSQL
- SQLAlchemy
- dotenv (highly recommended for database confidentiality)
- Virtualenv (optional but recommended)


## Project Structure

***Make sure that django/ and trip_scraper/ are in the same directory.***

```bash
root/
├── django/
│   ├── media/    # upon running the project, the migrated images will be stored in this folder.
│   │   └── property_images/
│   │       ├── 1/
│   │       │   └── 02269120009zuy22k7836.jpg
│   │       ├── 2/
│   │       │   └── 20091e000001f8rwc09D0.jpg
│   │       └── ....
│   ├── property_project/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── property_app/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── migrate_scrapy_data.py
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   │       └── property_app/
│   │           └── home.html
│   ├── manage.py
│   ├── .env
│   └── README.md
└── trip_scraper/
    └── trip_scraper/
        └── images/
            └── full/
                ├── 20091e000001f8rwc09D0.jpg
                ├── 32790a7467b64f12b5260fb480724f87.jpg
                └── ...
```

## Key Files and Directories
  - **property_app/models.py**: Contains the models for Property, Location, Amenity, and Image.
  - **property_app/admin.py**: Configures the Django admin interface for the application.
  - **property_app/management/commands/migrate_scrapy_data.py**: Custom management command to migrate data from a PostgreSQL database.
  - **property_app/templates/property_app/home.html**: Home page template.


## Setup Instructions

  1. **Clone the repository**:
  
      ```bash
      git clone https://github.com/nafiahossain/django.git
      cd django
      ```

  2. **Create and activate a virtual environment** (optional but recommended):
  
      Create a virtual environment and install dependencies:
      
      ```bash
      python3 -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```

  3. **Install dependencies**:

      ```bash
      pip install -r requirements.txt
      ```
      
      or,
     
      ```bash
      pip install django psycopg2-binary sqlalchemy python-dotenv pillow requests
      ```
     
  4. **Set up environment variables**:
  
      Ensure you have a .env (rename the .env.sample to .env, then add your credentials) file at the root of the Django project containing the following:
      
      ```env
      SECRET_KEY=your-secret-key

      DB_NAME=yourdatabase
      DB_USER=username
      DB_PASSWORD=password
      DB_HOST=localhost
      DB_PORT=5433
      
      DATABASE_URL=postgresql://username:password@localhost:5433/yourdatabase
      ```
      
      Ensure that your PostgreSQL server is running, and the database specified in the .env file exists.
     
  5. **Run migrations**:
  
      Apply the database migrations:
      
      ```bash
      python manage.py makemigrations property_app
      python manage.py migrate
      ```

  6. **Load initial scrapy data**:
  
      You can use the custom management command to migrate data from the existing PostgreSQL database. Before running this command, make sure to Replace your scrapy local image directory with the actual path where        it was stored. If, the django folder and the trip_scraper folder is in the same directory (as shown in the Project Structure), then keep it as it is.

      ```python
      # property_app/migrate_scrapy_data.py
  
      # Path to your local image directory
        LOCAL_IMAGE_DIR = os.path.join(settings.BASE_DIR, '../trip_scraper/trip_scraper/images/full/')
      ```
      
      After data migration, the images will be saved in this directory:

      ```python
      # property_project/settings.py.py
  
      # Media files (Images, etc)
      MEDIA_URL = '/media/'
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
      ```
      If you want, you can change this directory as per your need.
     
      If the scrapy image directory setup is done, then run this command to migrate data from the existing scrapy database:

     ```bash
      python manage.py migrate_scrapy_data
      ```

  8. **Create an admin user**:
  
      To use the admin panel, First you’ll need to create a user who can login to the admin site. Run the following command:
        
      ```bash
      python manage.py createsuperuser
      ```
    
      Enter your desired username, email address, and password. You will be asked to enter your password twice, the second time as a confirmation of the first. Using this info, you can log in to the admin panel and       perform CRUD operation on the migrated data.

  9. **Run the development server**:
  
      Start the Django development server:
      
      ```bash
      python manage.py runserver
      ```
    
      Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the application. To perfrom CRUD operation on data, you'll need to log in to the admin panel which is [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). 

     - Output:

        - Images: Images migrated and stored stored in a directory called `/media/`.
        - Database: Migrated hotel data stored in 'yourdatabase', in the PostgreSQL database.
        - Django Admin Interface: Migrated data can be seen on the admin interface.


## Usage
  - **Home Page**: The home page is accessible at the root URL [/](http://127.0.0.1:8000/).
  - **Admin Interface**: Access the Django admin at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage properties, locations, amenities, and images.


## Testing

After running the server, check the [Django admin interface](http://127.0.0.1:8000/admin/) to view all the migrated data. There will be three models, Properties, Amenities, and Locations. You can perform CRUD operations on these models. Also check your database and image directory whether the data was migrated or not. 


## Starting New Project (optional)

If you want to create a new django project, then run this following commands: 

    
     django-admin startproject property_project
    
This will create a property_project directory in your current directory. This establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

To verify your Django project works, run this following command:

    
    python manage.py runserver
    

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for discussion.
