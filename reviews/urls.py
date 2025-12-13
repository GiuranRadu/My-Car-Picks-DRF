from django.urls import path
from .views import (
    create_review,
    get_review,
    delete_review,
    modify_review,
    get_all_reviews,
    get_my_reviews,
)

# Create your views here.
urlpatterns = [
    path("create-review/", create_review, name="create-review"),
    path("get-review/<int:pk>/", get_review, name="get-review"),
    path("delete-review/<int:pk>/", delete_review, name="delete-review"),
    path("modify-review/<int:pk>/", modify_review, name="modify-review"),
    path("get-all-reviews/", get_all_reviews, name="get-all-reviews"),
    path("get-my-reviews/", get_my_reviews, name="get-my-reviews"),
]
