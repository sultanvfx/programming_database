from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Item(models.Model):
    """
    Item is the name of table.
    """
    name = models.CharField(max_length=32)  # example: 'python' Or 'css' Or 'java'
    description = models.TextField()  # example: 'python is simple programming' -Or- 'css styles html' -Or- 'java is very powerful'

    def __str__(self):
        return self.name


