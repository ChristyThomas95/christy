from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills', views.skills, name='skills'),
    path('projects', views.projects, name='projects'),
    path( 'projectdetails', views.projectdetails, name='projectdetails'),
    path('contact', views.contact, name='contact'),
]