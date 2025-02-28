from django.urls import path
from .views import post_detail, homepage  # Ensure homepage is correctly imported

app_name = "PostApp"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('post/<int:pk>/', post_detail, name="post_detail"),
]
