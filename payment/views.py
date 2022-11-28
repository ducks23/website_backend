from django.contrib.auth.models import User
from payment.apps.stripe_helper import Stripe
from payment.apps.mailgun import send_email
from rest_framework.response import Response
from rest_framework.views import APIView

from payment.apps.authentication import TokenAuth
from rest_framework.decorators import api_view


@api_view(http_method_names=["POST"])
def ping(request):
    return Response("ping")


class StripeView(APIView):
    authentication_classes = (TokenAuth,)
    client = Stripe()

class CreateStripeToken(StripeView):
    authentication_classes = (TokenAuth,)
    client = Stripe()

    def post(self, request):
        """
        Creates a token based on someones card info.
        A token is single use.
        """
        response = Stripe().create_token(request.data)
        return Response(response)

class CreateCharge(APIView):
    authentication_classes = (TokenAuth,)
    client = Stripe()

    def post(self, request):
        """
        Charges a sepcifc customer a certain amount.
        """
        response = Stripe().charge(data=request.data)
        return Response(response)


class UserManagement(APIView):
    """
    User Management Class
    """
    def post(self, request):
        data = request.data
        email = data["email"]
        first_name = data["first_name"]
        last_name = data["last_name"]
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
        return Response("subscribed")


class VerifyEmail(APIView):
    def post(self, request):
        """
        This will be an endpoint that takes in a hash and verifies
        that a user has received the email, then will redirect. No auth, maybe
        """
        return Response("Verified email")


class CustomerView(APIView):
    """
    View handles all customer operations
    """
    authentication_classes = (TokenAuth,)
    client = Stripe()

    def post(self, request):
        """
        Create a customer.
        """
        self.client.create_customer(request.data)
        return Response(200)

    def put(self, request):
        """
        Update a customers info.
        """
        self.client.update_customer(request.data)
        return Response(200)

    def delete(self, request):
        """
        Delete a customer.
        """
        self.client.delete_customer(request.data["customer_id"])
        return Response(200)

    def get(self, request):
        """
        Gets a list of customers, if a specific customer id is specifcied
        then it will retrieve their data
        """
        if customer_id := request.data.get("customer_id"):
            return Response(data=self.client.retrieve_customer(customer_id))
        response = self.client.list_customers()
        return Response(data=response, status=200)
