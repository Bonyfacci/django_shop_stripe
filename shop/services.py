import stripe

from config.settings import STRIPE_SECRET_KEY


def create_a_payment(item, url_path):
    stripe.api_key = STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': f'Товар: {item.name}',
                        'description': f'Описание товара: {item.description}',
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


def create_a_payment_intent(order):
    stripe.api_key = STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=int(float(order.tax_cost) * 100),
        currency='rub',
        description=f'Order: {order.id}, Total cost: {int(float(order.tax_cost) * 100)} RUB',
    )
    return {
        'clientSecret': intent['client_secret'],
        'description': intent['description'],
    }
