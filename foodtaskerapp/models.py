from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=500, default="Name")
    phone = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='restaurant_logo/', blank=False)

    def __str__(self):
        return self.name