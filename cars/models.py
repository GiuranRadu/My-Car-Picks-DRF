from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Car(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='cars')
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    year=models.PositiveIntegerField()
    image_urls=models.JSONField(default=list,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"