# importam clasa serializers din django restframework(drf) , aceasta ne ajuta sa transformam obicte python (modele) in JSON si invers
from rest_framework import serializers

# importam functia care returneaza modelul de utilizator folosit in proiect
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# get_user_model returneaza modelul de user activ in proiect, poate fi modelul default al django sau unul custom definit in settings.py prin AUTH_USER_MODEL

User = get_user_model()

# serializer pentru inregistrarea unui user nou


class RegisterSerializer(serializers.ModelSerializer):
    # clasa Meta defineste info despre modelul pe care il serializam
    password1 = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        # referire catre user
        model = User
        # serializerul nu ar sti nimic despre aceste campuri sau nu ar sti nimic daca nu le declaram
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

    def validate(self, data):
        errors = {}

        # verificare parole
        if data.get("password1") != data.get("password2"):
            errors["password"] = "Parolele nu coincid"
        # verificare first_name
        if not data.get("first_name"):
            errors["first_name"] = "First name is mandatory"
        if not data.get("last_name"):
            errors["last_name"] = "Last name is mandatory"

        #  data am strans erori, le arunca toate odata
        if errors:
            raise serializers.ValidationError(errors)

        # daca totul este ok, returnam data neschimbat
        return data

    def create(self, validated_data):
        password = validated_data.get("password1")

        # Eliminam pass1 si 2 din dictionarul principal
        validated_data.pop("password1", None)
        validated_data.pop("password2", None)

        # Creem userul cu metoda create_user() -> Aceasta metoda hash-ueste automat parola
        user = User.objects.create_user(password=password, **validated_data)

        return user


#!Important
# Serializers vine din biblioteca drf.
# Este sistemul care transforma intre obiecte py si formate transferabile cum ar fi JSON
# PS : Gandeste l ca pe un translator intre lumea interna a aplicatiei (modele) si lumea exterioara (frontend postman api-uri)


# Ce face create_user() -> ea cheama intern set_password() -> aceasta hash-uieste folosint algoritmul SHA256


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Vezi TokenObtainPairSerializer -> TokenObtainSerializer -> getToken are decoratorul @classmethod.
    # get_token() -> este o metoda legata de CLASA, nu de instanta -> de acea primeste param cls si nu self
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_staff"] = user.is_staff
        token["lala"] = "lala-band"
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        
        data["user"] = {
            "id": self.user.id,
            "email": self.user.email,
            "username": self.user.username,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
        }

        return data
