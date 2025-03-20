from django.urls import path
from .views import book_turf, cancel_booking

urlpatterns = [
    path('book/', book_turf, name='book_turf'),
    path('cancel/', cancel_booking, name='cancel_booking'),
]
