from django.db import models

# Create your models here.
class create_event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    liked = models.BooleanField(default=False)
