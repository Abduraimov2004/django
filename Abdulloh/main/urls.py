from django.urls import path
from .views import main

urlpatterns = [
    path('', main),  # Root URL maps to index_view
]
