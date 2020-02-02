from django.urls import path
from .views import CarsList

urlpatterns = [
    path('', CarsList.as_view(), name='cars-list'),
]