from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.app_detail, name="app_detail"),  # Ensure the view name matches here
]
