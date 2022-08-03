# to deploy
```
export STRIPE_API_KEY="your_test_key"
export MAIL_GUN_KEY="your_mailgun_key"
python3 manage.py runserver
```

## api use
```
curl -X POST -H "Content-Type: application/json"  -d '{"number": 2, "cvc": 3, "exp_month": 3, "exp_year": 2023}' http://127.0.0.1:8000/create_token
```
