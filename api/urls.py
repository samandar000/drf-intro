from django.urls import path
from .views import hi

urlpatterns = [
    path('hi', hi),
]
