from django.urls import path
from . import views


app_name = 'ride'

urlpatterns = [
    path('', views.ride_list, name='home'),

]
