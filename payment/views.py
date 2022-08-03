from urllib import response
from django.http import HttpResponse
from django.contrib.auth.models import User
from payment.apps.stripe_helper import Stripe
from payment.apps.mailgun import send_email
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateStripeToken(APIView):
    def post(self, request):
        data = request.data
        client = Stripe()
        try:
            response = client.create_token(
                number=data["number"],
                exp_month=data["exp_month"],
                exp_year=data["exp_year"],
                cvc=data["cvc"],
            )
        except Exception as err:
            return Response(404)

        return Response("hello")


class CreateSubscription(APIView):
    def post(self, request):
        return Response("subscribed")

    def delete(self, request):
        return Response("deleted")


class UserManagement(APIView):
    def post(self, request):
        data = request.data
        email = data["email"]
        first_name = data["first_name"]
        last_name = data["last_name"]

        # create random hash in email to be received in verify email endpoint
        response = send_email(email=email, name=first_name + " " + last_name)
        if response.status_code != 200:
            return Response("Invalid email address")

        User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=data["password"],
        )

        try:
            user = User.objects.get(username=data["username"])
        except User.DoesNotExist:
            return Response(500)

        # user add permissions

        return Response("subscribed")

    def update(self, request):
        return Response("Update password")

    def delete(self, request):
        return Response("delete user")


class VerifyEmail(APIView):
    def post(self, request):
        """
        This will be an endpoint that takes in a hash and verifies
        that a user has received the email, then will redirect. No auth, maybe
        """
        return Response("Verified email")
