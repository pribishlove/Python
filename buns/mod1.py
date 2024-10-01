import requests

response = requests.get("https://fakestoreapi.com/products")
products = response.json()

cheap_products = [product for product in products if product['price'] < 20]

for product in cheap_products:
    print(product)

response = requests.get("https://fakestoreapi.com/products/categories")
categories = response.json()

for category in categories:
    print(category)

response = requests.get("https://fakestoreapi.com/products/category/jewelery")
jewelery_products = response.json()

for product in jewelery_products:
    print(product)

response = requests.get("https://fakestoreapi.com/users")
users = response.json()

for user in users:
    print(user)

new_user = {
    "email": "max@example.com",
    "username": "maksim_makushkin",
    "password": "password123",
    "name": {
        "firstname": "Maxim",
        "lastname": "Makushkin"
    },
    "address": {
        "city": "Moscow",
        "street": "Main Street",
        "number": 123,
        "zipcode": "10001",
        "geolocation": {
            "lat": "40.7128",
            "long": "-74.0060"
        }
    },
    "phone": "555-1234"
}

response = requests.post("https://fakestoreapi.com/users", json=new_user)