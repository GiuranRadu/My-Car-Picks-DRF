"""
URL configuration for MyCarPicks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import home_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("cars/", include("cars.urls")),
    path("reviews/", include("reviews.urls")),
    # il adaugi aici
    path("", home_view),  # 👈 HOME VIEW "/"

]

# static() este un helper Django folosit doar in development -> static() este un fake Nginx , doar ca sa vezi rezultatul rapid. 
from django.conf.urls.static import static


# In development, Django va servi fisierere media (imagini/fisiere, etc) folosind serverul sau intern. Serveste media doar ca sa evitam configurarea un CDN (web server , cum ar fi Cloudfare sau Cloundinary)
# In productie acest lucru se face cu Nginx / Apache / CDN, nu DJANGO. Django trebuie sa generele doar JSON. 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
