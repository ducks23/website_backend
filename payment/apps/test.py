import jwt

encoded_jwt = jwt.encode({"user": "john"}, "dont_tell_anyone", algorithm="HS256")

print(encoded_jwt)

print(jwt.decode(encoded_jwt, "dont_tell_anyone", algorithms=["HS256"]))
