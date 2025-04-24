from django.db import models

# Create your models here.
class User(models.Model):
    # location = models.IntegerField()
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    data_refer = models.CharField(max_length=100)
    cost = models.IntegerField()
    kw = models.IntegerField()

    def __str__(self):
        return self.name

