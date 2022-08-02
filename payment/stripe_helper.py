import stripe
import os

class Stripe:

    stripe.api_key = os.environ['STRIPE_API_KEY']

    def create_customer(self, name, address, email):
        resp = stripe.Customer.create(name=name, address=address, email=email)
        return resp

    def get_balance(self):
        return stripe.Balance.retrieve()

    def charge(self, amount):
        resp = stripe.Charge.create(
          amount=2000,
          currency="usd",
          source="tok_amex",
          description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
        )
        return resp

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

    def create_charge(self, amt, src, description):
        resp = stripe.Charge.create(
            amount=amt,
            currency="usd",
            source=src,
            description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
        )
        return resp


n = "Maxamillion"

addr = {'state': "TX"}
email = 'testemail@gmail.com'
cls = Stripe()
#token = cls.create_token("4242424242424242", 8, 2025, 622)
#print(f" token: {token}")

print(cls.get_balance())
