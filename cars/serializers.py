from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = [              
            "brand",
            "model",
            "year",
            "image_urls",
            "created_at"
        ]
    
    
    
    def validate(self , data):
        errors = {}
        
        if data.get('year') < 1950:
            errors['year'] = "Anul trebuie sa fie mai mare de 1950"
        
        if errors:
            raise serializers.ValidationError(errors)

        return data
    
