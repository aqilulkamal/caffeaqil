from django.db import models

# Create your models here.
class Coffe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name