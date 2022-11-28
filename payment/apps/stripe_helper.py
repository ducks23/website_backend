import stripe
import os

TEST_CARD = "4242424242424242"


class Stripe:

    stripe.api_key = os.environ["STRIPE_API_KEY"]

    def create_customer(self, data):
        address = {
            "city": data["city"],
            "country": data["country"],
            "line1": data["line1"],
            "postal_code": data["postal_code"],
            "state": data["state"],
        }
        resp = stripe.Customer.create(name=data['name'], address=address, email=data['email'])
        return resp

    def update_customer(self, data):
        return stripe.Customer.modify(
            sid=data.get("customer_id"),
            name=data.get("name"),
            address=data.get("address"),
            email=data.get("email"),
        )

    def retrieve_customer(self, customer_id):
        return stripe.Customer.retrieve(customer_id)

    def list_customers(self):
        response = stripe.Customer.list()
        return [(data["name"], data["id"]) for data in response["data"]]

    def delete_customer(self, customer_id):
        return stripe.Customer.delete(customer_id)

    def get_balance(self):
        return stripe.Balance.retrieve()

    def create_token(self, data):
        resp = stripe.Token.create(
            card={
                "number":data["number"],
                "exp_month":data["exp_month"],
                "exp_year":data["exp_year"],
                "cvc": data["cvc"],
            }
        )
        return resp

    def charge(self, data):
        resp = stripe.Charge.create(
            currency="usd",
            description="Test Charge",
            amount=data["amount"],
            source=data["src"],
        )
        return resp
