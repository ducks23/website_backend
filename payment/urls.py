from django.urls import path
from payment import views

urlpatterns = [
    path("create_token", views.CreateStripeToken.as_view()),
    path("customer", views.CustomerView.as_view()),
    path("ping", views.ping),
]
