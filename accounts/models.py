from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# In mod normal modelul AbstractUser are : USERNAME_FIELD = 'username' , REQUIERED_FIELDS = 'email'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    username = models.CharField(
        ("username"),
        max_length=150,
        unique=False,
        help_text=("required 150ch or fewer"),
    )
    
    #NOTE: implicit django va crea numele tabelei <app_label>_<model_name_lowercase>, pentru a evita conflicte intre aplicatii diferite care pot acea acelasi model.
    
    class Meta:
        db_table = "users"
        verbose_name = "Samsar"
        verbose_name_plural = "Samsari"
        
        
    def __str__(self):
        return self.username + "Samsarul"
    
    
# !IMPORTANT
# In vederea modificarii default User -> avem 2 variante:
# CustomUser al nostru poate sa faca inherit la 2 clase:
# 1. AbstractUser -> extindem modelul CURENT (noi pe asta o folosim)
# 2. AbstractBaseUser -> unde creem totul de la0, acest approach ne ofera mai mult control pe ceea ce facem, dar necesita mult mai multa munca.