from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Car(models.Model):
    creator = models.ForeignKey(User , on_delete=models.CASCADE , related_name='cars')
    brand = models.CharField(
        max_length=150,
        help_text=("required 150ch or fewer"),
    )
    model = models.CharField(
        max_length=150,
        help_text=("required 150ch or fewer"),
    )
    year = models.IntegerField(
        help_text=("required 1950 or higher")
    )
    image_urls = models.JSONField(default=list , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    