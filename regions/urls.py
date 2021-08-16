from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('asia', asia, name='asia'),
    path('country_create/', create, name='country_create'),
    path('delete/<int:pk>', delete, name="country_delete"),
    path('update/<int:pk>', update, name="country_update"),
]