# c1/urls.py
from django.urls import path
from .views import ContactListCreateView

urlpatterns = [
    path('contact/', ContactListCreateView.as_view(), name='contact-create'),  # Здесь не забудьте указать конечный путь
]
