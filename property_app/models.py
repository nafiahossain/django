from django.db import models
import os


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False)  # Required
    rating = models.CharField(max_length=255, blank=True, null=True)  # Optional
    description = models.TextField(blank=True, null=True)  # Optional
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    locations = models.ManyToManyField('Location', blank=True)  # Optional
    address = models.TextField(blank=True, null=True)  # Optional
    amenities = models.ManyToManyField('Amenity', blank=True)  # Optional

    def __str__(self):
        return self.title


def get_image_path(instance, filename):
    return os.path.join('property_images', str(instance.property.property_id), filename)


class Image(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)  # Optional

    def __str__(self):
        return f"Image for {self.property.title}"
    

class Location(models.Model):
    LOCATION_TYPES = [
        ('country', 'Country'),
        ('state', 'State'),
        ('city', 'City'),
    ]
    name = models.CharField(max_length=255, unique=True, blank=False)  # Required
    type = models.CharField(max_length=10, choices=LOCATION_TYPES, blank=False)  # Required
    latitude = models.FloatField(blank=True, null=True)  # Optional)
    longitude = models.FloatField(blank=True, null=True)  # Optional)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Amenity(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)  # Required

    def __str__(self):
        return self.name