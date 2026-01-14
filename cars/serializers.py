from rest_framework import serializers
from .models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["id", "image", "created_at"]


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    # is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = [
            "id",
            # 'is_owner',
            "brand",
            "model",
            "year",
            "created_at",
            "images",
        ]

    # def get_is_owner(self, obj):
    #     return self.context["request"].user == obj.creator

    def validate(self, data):
        errors = {}

        if data.get("year") < 1950:
            errors["year"] = "Anul trebuie sa fie mai mare de 1950"

        if errors:
            raise serializers.ValidationError(errors)

        return data
