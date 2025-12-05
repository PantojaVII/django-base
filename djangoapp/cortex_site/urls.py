from django.urls import path
from . import views

app_name = 'cortex_site'

urlpatterns = [
    path('', views.home_view, name='home'),
]