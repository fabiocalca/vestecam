import mercadopago
sdk = mercadopago.SDK("ENV_ACCESS_TOKEN")

payment_data = {
    "transaction_amount": 1,
    "description": "Título do produto",
    "payment_method_id": "pix",
    "payer": {
        "email": "test@test.com",
        "first_name": "Fabio",
        "last_name": "Calca Carvalho",
        "identification": {
            "type": "CPF",
            "number": "36142178840"
        },
        "address": {
            "zip_code": "06233-200",
            "street_name": "Av. das Nações Unidas",
            "street_number": "3003",
            "neighborhood": "Bonfim",
            "city": "Osasco",
            "federal_unit": "SP"
        }
    }
}

payment_response = sdk.payment().create(payment_data)
payment = payment_response["response"]
print(payment)