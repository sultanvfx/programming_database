from django.contrib import admin

# Register your models here.
from pdb_app.models import Item, Category

admin.site.register(Item)
admin.site.register(Category)
