from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('asia/', asia, name='asia'),
    path('europe/', europe, name='europe'),
    path('north-america/', north_america, name='north-america'),
    path('south-america/', south_america, name='south-america'),
    path('africa/', africa, name='africa'),
    path('oceania/', oceania, name='oceania'),
    path('country_create/', create, name='country_create'),
    path('delete/<int:pk>', delete, name="country_delete"),
    path('update/<int:pk>', update, name="country_update"),
]