from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    # cautam direct in cookie deoarece nu mai folosim auth bearer
    def authenticate(self, request):
        raw_token = request.COOKIES.get("access_token")
        # daca nu este cookie inseamna ca nu esti autentificat
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token
