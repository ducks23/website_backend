from django.urls import path
from payment import views

urlpatterns = [
    path('create_token', views.CreateToken.as_view()),
    
]