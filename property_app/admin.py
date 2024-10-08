from django.contrib import admin
from django.utils.html import format_html
from .models import Property, Image, Location, Amenity


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;" />', obj.image.url)
        return "No Image"

    image_tag.short_description = 'Image Preview'


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'title', 'rating', 'image_tag', 'create_date', 'update_date')
    list_display_links = ('property_id', 'title')
    filter_horizontal = ('locations', 'amenities')
    inlines = [ImageInline]
    list_filter = ['create_date']
    search_fields = ['title']

    def image_tag(self, obj):
        first_image = obj.images.first()  # Assuming `images` is a related name for the Image model
        if first_image and first_image.image:
            return format_html('<img src="{}" style="max-width: 80px; max-height: 80px;" />', first_image.image.url)
        return "No Image"

    image_tag.short_description = 'Image'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'latitude', 'longitude')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'type',]


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ['name',]


# Don't need to register Image separately as it's inline with Property