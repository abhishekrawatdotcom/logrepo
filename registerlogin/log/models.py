from django.db import models

# Create your models here.
class EMPMODEL(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=59)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
