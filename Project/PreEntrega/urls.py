from django.urls import path
from . import views

app_name = 'PreEntrega'

urlpatterns = [
    path ('', views.home, name='home'),
]