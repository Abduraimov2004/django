from django.urls import path
from .views import car, companiy, p_language

urlpatterns = [
    path('car', car),
    path('companiy', companiy),
    path('p_language', p_language),

]
