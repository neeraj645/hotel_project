
from .views import *
from django.urls import path

urlpatterns = [
    path("api/get-hotels/", get_hotel),
    path('home/', home),
]
