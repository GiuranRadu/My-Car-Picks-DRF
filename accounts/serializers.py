#importam clasa serializers din django restframework(drf) , aceasta ne ajuta sa transformam obicte python (modele) in JSON si invers
from rest_framework import serializers

#importam functia care returneaza modelul de utilizator folosit in proiect
from django.contrib.auth import get_user_model

#get_user_model returneaza modelul de user activ in proiect, poate fi modelul default al django sau unul custom definit in settings.py prin AUTH_USER_MODEL

User = get_user_model()

#serializer pentru inregistrarea unui user nou

class RegisterSerializer(serializers.ModelSerializer):
#clasa Meta defineste info despre modelul pe care il serializam
    class Meta:
        model = User #legam serializerul de modelul User
        fields = ['email' , 'username' , 'password'] #definim ce campuri vor fi incluse in request / response
        #extra_kwargs ne permita sa modificam comportamentul unui camp. In cazul de fata parola nu se va afisa niciodata in raspunsul JSON
        extra_kwargs = {
            "password" : {
                "write_only" : True
            }
        }
        
    def create(self, validated_data):
        # folosim metoda create_user care hash -ueste automat parola (nu o salveaza in clar)
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']
        )
        
        # returnam obiectul user create pentru a fi trimis inapoi in raspuns
        return user