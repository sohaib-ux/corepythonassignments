def calculate_total(cart_items):
    if not cart_items:
        return "The cart is empty"
    
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total *= 0.9
    
    return total

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total_price = calculate_total(cart_items)
print(total_price)
