from django.urls import path
from .views import generate_passwords_view, recover_passwords_view

urlpatterns = [
    path('generate-passwords/', generate_passwords_view, name='generate-passwords'),
    path('recover-passwords/', recover_passwords_view, name='recover-passwords'),
]