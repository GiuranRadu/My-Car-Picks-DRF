from rest_framework import serializers
from .models import Review
from cars.serializers import CarSerializer
from accounts.serializers import RegisterSerializer


class ReviewSerializer(serializers.ModelSerializer):
    # * nested serializers
    # car = CarSerializer(read_only=True)
    # author = RegisterSerializer(read_only=True)
    class Meta:
        model = Review

        # ⭐ fields = lista completa a campurilor care vor aparea în JSON-ul API
        # Practic îi spui lui DRF: "serializează DOAR aceste câmpuri".
        # ORICE nu e aici -> nu ajunge în request/response.
        fields = [
            "id",
            "car",
            "author",
            "rating",
            "content",
            "created_at",
            "updated_at",
        ]

        # ⭐ read_only_fields = campuri care NU pot fi modificate prin API
        # DRF le va include în răspuns, dar nu le va accepta în POST/PATCH.
        # Motive:
        # - `id` este generat de DB, deci nu îl trimitem din frontend
        # - `author` se setează automat din request.user
        # - `created_at` și `updated_at` sunt generate de Django, nu de client
        #
        # Dacă NU le marchezi read-only, un user ar putea încerca să le modifice,
        # iar DRF ar arunca erori.
        read_only_fields = ["id", "author", "created_at", "updated_at"]
