from django.db import models
from django.contrib.auth import get_user_model
import os
import uuid

User = get_user_model()
# Create your models here.


class Car(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")
    brand = models.CharField(
        max_length=150,
        help_text=("required 150ch or fewer"),
    )
    model = models.CharField(
        max_length=150,
        help_text=("required 150ch or fewer"),
    )
    year = models.IntegerField(help_text=("required 1950 or higher"))
    image_urls = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


def upload_path(instance, filename):
    # instance = obiectul modelului care este salvat acum
    # nume unic ca sa eviti coliziuni: <uuid>.<ext>
    # os.path.splitext -> Returneaza un tuple cu 2 elemente ->(filename_fara_extensie, extensie)
    # poza_mea.jpg -> (poza_mea, jpg)
    print(f"🔴🔴🔴 -> {os.path.splitext(filename)}")
    ext = os.path.splitext(filename)[1].lower()
    return f"cars/{instance.car_id}/{uuid.uuid4()}{ext}"


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=upload_path)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"CarImage {self.id} from Car {self.car_id}"
