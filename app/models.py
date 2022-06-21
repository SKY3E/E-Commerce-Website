from email.mime import image
from django.db import models
from django.db.models import Model

# Create your models here.
class item(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False)
  details = models.CharField(max_length=1000, blank=True, null=True)
  price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=20)
  tag_choices = (
    ('Bakery', 'Bakery'),
    ('Meat&Seafood', 'Meat&Seafood'),
    ('Fruits', 'Fruits'),
    ('Vegetables', 'Vegetables'),
    ('Dairy', 'Dairy')
  )
  tag = models.CharField(max_length=100, default=None, blank=False, null=False, choices=tag_choices)
  image = models.ImageField(default=None, blank=False, null=False, upload_to='files-pictures')