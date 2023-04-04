from django.urls import path
from .views import hi,addition,subtract,multiply,devide

urlpatterns = [
    path('hi', hi),
    path('add',addition),
    path('subtract',subtract),
    path('multiply',multiply),
    path('devide',devide)
]
