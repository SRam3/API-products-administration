from products import products

def get_items_with_name(name):
    return [product for product in products if product['name'] == name] 