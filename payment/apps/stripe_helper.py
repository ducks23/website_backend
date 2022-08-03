import stripe
import os


class Stripe:

    stripe.api_key = os.environ["STRIPE_API_KEY"]

    def create_customer(self, name, address, email):
        resp = stripe.Customer.create(name=name, address=address, email=email)
        return resp

    def get_balance(self):
        return stripe.Balance.retrieve()

    def create_token(self, number, exp_month, exp_year, cvc):
        resp = stripe.Token.create(
            card={
                "number": number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            },
        )
        return resp

    def charge(self, amount, src):
        resp = stripe.Charge.create(
            amount=amount,
            currency="usd",
            source=src,
            description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
        )
        return resp
