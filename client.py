import requests
import os
import jwt
import json


class CustomerClient:
    def __init__(self, user):
        self.url = "http://127.0.0.1:8000/customer"
        self.secret = os.environ["TOKEN_SECRET"]
        self.user = user

    def call(self, method, data=None):
        headers = {"Authorization": self.create_token(self.user)}
        try:
            response = requests.request(
                method=method, url=self.url, data=data, headers=headers
            )
        except Exception as err:
            print(f"error: {err}")
            return
        return response.content

    def create_token(self, email=None):
        return jwt.encode({"user": email}, self.secret, algorithm="HS256")

    def post(self, name, email, city, country, line1, zip_code, state):
        data = {
            "city": city,
            "email": email,
            "name": name,
            "country": country,
            "line1": line1,
            "postal_code": zip_code,
            "state": state,
        }
        return self.call("POST", data)

    def update(self, name, email, city, country, line1, zip_code, state, customer_id):
        data = {
            "customer_id": customer_id,
            "city": city,
            "email": email,
            "name": name,
            "country": country,
            "line1": line1,
            "postal_code": zip_code,
            "state": state,
        }
        return self.call("PUT", data)

    def delete(self, customer_id):
        return self.call("DELETE", customer_id)

    def get(self, customer_id=None):
        data = {"customer_id": customer_id}
        return self.call("GET", data=data)


client = CustomerClient("admin")

all_customers = json.loads(client.get())

print(all_customers)

for x in all_customers:
    print(x)

first_customer = all_customers[0][1]

print(f"customer id = {first_customer}")

client.update(
    "matt", "test@email.com", "hello", "US", "main st", "97008", "OR", first_customer
)
