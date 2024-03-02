import stripe

from config.settings import STRIPE_SECRET_KEY


def create_a_payment(item, url_path):
    stripe.api_key = STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': "usd",
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=f'{url_path}success/',
        cancel_url=f'{url_path}cancel/',
    )
    return session.url

