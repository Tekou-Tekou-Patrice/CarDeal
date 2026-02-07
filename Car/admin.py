from django.contrib import admin
from . models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('status', 'nom', 'marque', 'prix')
    list_filter = ('status',)
    search_fields = ('nom','marque','prix')

admin.site.register(Car)
