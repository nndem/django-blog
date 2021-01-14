from django.urls import path
from . import views

urlpatterns = [
	path('', views.my_contacts, name='my_contacts'),
	]