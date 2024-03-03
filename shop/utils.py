
def calculate_price(items):
    if items is not None:
        total_cost_rub = 0
        for item in items:
            if item.currency == 'USD':
                total_cost_rub += item.price * 90
            elif item.currency == 'EUR':
                total_cost_rub += item.price * 100
            else:
                total_cost_rub += item.price
        return total_cost_rub
