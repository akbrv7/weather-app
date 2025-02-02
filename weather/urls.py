from django.urls import path
from .views import *
urlpatterns = [
    path('', weather_veiw, name="weather_home"),
]