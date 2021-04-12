from django.urls import path
from .views import BloombergDashAPI


urlpatterns = [
    path('bloomberg_api.html', BloombergDashAPI, name='bloomberg-dash'),
    ]