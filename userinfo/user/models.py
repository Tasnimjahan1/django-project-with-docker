from django.db import models


# Create your models here.
class UserInfo(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=250, null=True, blank=True)
    cuntry = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    email = models.EmailField()
