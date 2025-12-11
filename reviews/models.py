from django.db import models
from django.contrib.auth import get_user_model
from cars.models import Car
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")    
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    content = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
    #     db_table = "car_reviews"
    #     ordering = ["-created_at"]
        verbose_name = "Recenzie"
        verbose_name_plural = "Recenzii"

    def __str__(self):
        return f"Review by {self.author} for {self.car}"