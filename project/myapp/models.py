from django.db import models

# Create your models here.
# class About:
#    name: str
#    details: str
#    phone: int
#    email: str

# it will assign id automatically
class About(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone = models.IntegerField()
    email = models.CharField(max_length=100)