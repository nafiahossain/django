# Property Management System

This Django-based Property Management System allows users to manage property listings, including their locations, amenities, images, and more. The application supports scraping hotel data from a legacy PostgreSQL database and displays it in the Django admin interface.


## Features
  - Property Management: Create, update, and delete property records with details like title, rating, locations, amenities, and images.
  - Location & Amenities Management: Manage locations (city, state, country) and amenities related to properties.
  - Image Management: Upload and display images associated with each property in the admin interface.
  - Data Migration: Custom management command to migrate data from an existing PostgreSQL database, including local images.
  - Admin Interface: Enhanced admin interface to display property details, including images.


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
home/
├── django/
│   └── property_project/
│       ├── media/    # upon running the project, the migrated images will be stored in this folder.
│       │   └── property_images/
│       │       ├── 1/
│       │       │   └── 02269120009zuy22k7836.jpg
│       │       ├── 2/
│       │       │   └── 20091e000001f8rwc09D0.jpg
│       │       └── ....
│       ├── property_project/
│       │   ├── __init__.py
│       │   ├── asgi.py
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── wsgi.py
│       ├── property_app/
│       │   ├── __init__.py
│       │   ├── admin.py
│       │   ├── apps.py
│       │   ├── management/
│       │   │   └── commands/
│       │   │       └── migrate_scrapy_data.py
│       │   ├── migrations/
│       │   ├── models.py
│       │   ├── tests.py
│       │   ├── urls.py
│       │   ├── views.py
│       │   └── templates/
│       │       └── property_app/
│       │           └── home.html
│       ├── manage.py
│       ├── .env
│       └── README.md
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
  
      Ensure you have a .env file at the root of the project containing the following:
      
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
      cd property_project
      python manage.py makemigrations property_app
      python manage.py migrate
      ```

  6. **Load initial scrapy data**:
  
      You can use the custom management command to migrate data from the existing PostgreSQL 
      database:
        
      ```bash
      python manage.py migrate_scrapy_data
      ```

  7. **Create an admin user**:
  
      To use the admin panel, First you’ll need to create a user who can login to the admin site. Run the following command:
        
      ```bash
      python manage.py createsuperuser
      ```
    
      Enter your desired username, email address, and password. You will be asked to enter your password twice, the second time as a confirmation of the first. Using this info, you can log in to the admin panel and       perform CRUD operation on the migrated data.

  8. **Run the development server**:
  
      Start the Django development server:
      
      ```bash
      python manage.py runserver
      ```
    
      Visit http://127.0.0.1:8000/ to see the application.


## Usage
  - **Home Page**: The home page is accessible at the root URL [/](http://127.0.0.1:8000/).
  - **Admin Interface**: Access the Django admin at [/admin/](http://127.0.0.1:8000/admin/) to manage properties, locations, amenities, and images.


