from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
     path('registration-success/', views.registration_success, name='registration_success'),

]

