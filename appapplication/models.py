from django.db import models


class Bottle(models.Model):
    bottleid = models.CharField(max_length=50, primary_key=True)
    bottlename = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    pictureurl = models.CharField(max_length=100)

