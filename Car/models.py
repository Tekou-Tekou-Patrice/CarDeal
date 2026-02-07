from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os

# Create your models here.
STATUS = ((0,"Draft"),(1,"published"))

class Car(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    marque =  models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    proprio = models.ForeignKey(User, on_delete=models.CASCADE, related_name="car_proprio")
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    image = models.ImageField(upload_to="car/", null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.nom

@receiver(pre_delete, sender=Car)
def delete_car(sender, instance, **kwargs):
    if instance.image:
      if os.path.isfile(instance.image.path):
          os.remove(instance.image.path)
