from django.contrib import admin

from listings.models import Band
from .models import Band, Listing
admin.site.register(Band)
admin.site.register(Listing)

class ListingAdmin(admin.ModelAdmin):
     list_display = ('title, band')
