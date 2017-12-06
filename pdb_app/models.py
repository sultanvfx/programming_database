from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    """
    Category is the name of the table to be created in the sqlite3 database.
    Here Category can be: 'IDE', 'Programming Language'
    """

    class Meta:
        """
        This class is created to rectify the plural name 'Categorys' to 'Categories' in the admin page.
        """
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Item is the name of table to be created in the sqlite3 database.
    Here Item can be: 'Java', 'C++', 'PyCharm', 'Eclipse', 'Python'
    """
    name = models.CharField(max_length=32)  # example: 'python' Or 'css' Or 'java'
    description = models.TextField()  # example: 'python is simple programming' -Or- 'css styles html' -Or- 'java is very powerful'
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

