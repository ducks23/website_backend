from django.http import HttpResponse
from payment.stripe_helper import Stripe
import stripe, logging
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateToken(APIView):
    def post(self, request):
        data = request.data
        client = Stripe()
        try:
            response = client.create_token(
                number=data['number'],
                exp_month=data['exp_month'],
                exp_year=data['exp_year'],
                cvc=data['cvc']
            )
        except Exception as err:
            return Response(404)

        return Response("hello")