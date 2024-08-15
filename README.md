# Property Management System

This Django-based Property Management System allows users to manage property listings, including their locations, amenities, images, and more. The application supports scraping hotel data from a PostgreSQL database and displays it in the Django admin interface.

## Project Structure

```bash
home/
├── django/
│   └── property_project/
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
│       │   └── views.py
│       ├── templates/
│       │   └── property_app/
│       │       └── home.html
│       ├── db.sqlite3
│       ├── manage.py
│       ├── .env
│       └── README.md
└── scrapy/
    └── trip_scraper/
        └── images/
            └── full/
                ├── 20091e000001f8rwc09D0.jpg
                ├── 32790a7467b64f12b5260fb480724f87.jpg
                └── ...
```

## Features
  - Property Management: Create, update, and delete property records with details like title, rating, locations, amenities, and images.
  - Location & Amenities Management: Manage locations (city, state, country) and amenities related to properties.
  - Image Management: Upload and display images associated with each property in the admin interface.
  - Data Migration: Custom management command to migrate data from an existing PostgreSQL database, including local images.
  - Admin Interface: Enhanced admin interface to display property details, including images.


## Setup Instructions

  1. Clone the repository:
  
  ```bash
  git clone <repository-url>
  cd Nafia_SEIntern/django_1/property_project
  ```

  2. Install dependencies:
  
  Create a virtual environment and install dependencies:
  
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt
  ```

  3. Configure environment variables:
  
  Ensure you have a .env file at the root of the project containing the following:
  
  ```plaintext
  SECRET_KEY=your-secret-key

  DB_NAME=your_db_name
  DB_USER=your_username
  DB_PASSWORD=your_password
  DB_HOST=localhost
  DB_PORT=5432
  
  DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_db_name
  ```
  4. Run migrations:
  
  Apply the database migrations:
  
  ```bash
  python manage.py makemigrations property_app
  python manage.py migrate
  python manage.py migrate_scrapy_data
  python manage.py runserver
  ```

  5. Load or scrape initial data:
  
  You can use the custom management command to migrate data from the existing PostgreSQL 
  database:
    
  ```bash
  python manage.py migrate_scrapy_data
  ```

  6. Run the development server:
  
  Start the Django development server:
  
  ```bash
  python manage.py runserver
  ```

  Visit http://127.0.0.1:8000/ to see the application.


## Usage
  Admin Interface: Access the Django admin at /admin/ to manage properties, locations, amenities, and images.
  Home Page: The home page is accessible at the root URL /.


## Key Files and Directories
  property_app/models.py: Contains the models for Property, Location, Amenity, and Image.
  property_app/admin.py: Configures the Django admin interface for the application.
  property_app/management/commands/migrate_scrapy_data.py: Custom management command to migrate data from a PostgreSQL database.
  property_app/templates/property_app/home.html: Home page template.
  

