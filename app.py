from flask import Flask, jsonify, request
from products import products
from helpers import get_items_with_name

app = Flask(__name__)


@app.route("/")
def welcome():
    return jsonify({"message": "Welcome to Arenillo coffee shop"})


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify({"products": products, "message": "Product's list"})


@app.route("/products/<string:product_name>")
def get_product(product_name: str):
    """
    Obtain product information

    :param product_name: name to check
    :type product_name: str
    :return: First value from product_found's list
    """
    product_found = get_items_with_name(product_name)
    if len(product_found) > 0:
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "Product not found"})

@app.route("/products/<string:product_name>/description")
def get_product_description(product_name: str):
    """
    Obtain product information

    :param product_name: name to check
    :type product_name: str
    :return: First value from product_found's list
    """
    product_found = get_items_with_name(product_name)
    if len(product_found) > 0:
        return jsonify({"product": product_found[0]["description"]})
    return jsonify({"message": "Product not found"})


@app.route("/products", methods=["POST"])
def add_product():
    """Create a new product: Using Postman POST request"""
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"],
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})


@app.route("/products/<string:product_name>", methods=["PUT"])
def edit_product(product_name):
    """Update product properties, name, price or quantity: Using Postman PUT request"""
    product_found = get_items_with_name(product_name)
    if len(product_found) > 0:
        product_found[0]["name"] = request.json["name"]
        product_found[0]["price"] = request.json["price"]
        product_found[0]["quantity"] = request.json["quantity"]
        product_found[0]["presentation"] = request.json["presentation"]
        product_found[0]["description"] = request.json["description"]
        return jsonify(
            {
                "message": "Product Updated",
                "product": product_found[0],
            }
        )
    return jsonify({"message": "Product not found"})


@app.route("/products/<string:product_name>/price", methods=["PUT"])
def edit_product_price(product_name):
    """Update product price: Using Postman PUT request"""
    product_found = get_items_with_name(product_name)
    if len(product_found) > 0:
        product_found[0]["price"] = request.json["price"]
        return jsonify(
            {
                "message": "Product Updated",
                "product": product_found[0],
            }
        )
    return jsonify({"message": "Product not found"})


@app.route("/products/<string:product_name>", methods=["DELETE"])
def delete_product(product_name):
    """Delete a product from its name: Using Postman DELETE"""
    product_found = get_items_with_name(product_name)
    if len(product_found) > 0:
        products.remove(product_found[0])
        return jsonify({"message": "Product Deleted", "products": products})
    return jsonify({"message": "Product not found"})


@app.route("/products/sum-stock")
def sum_stock():
    """Calculate the total value of each element and returns the sum of them"""
    total = {
        product["name"]: product["price"] * product["quantity"] for product in products
    }
    return jsonify({"message": "The total value of your stock is:", "total": total})


@app.route("/products/sum-stock/<string:product_name>")
def sum_stock_by_name(product_name):
    """Calculate the total value of each element and returns the sum of them"""
    product_found = get_items_with_name(product_name)
    if len(product_found) > 0:
        total = product_found[0]["price"] * product_found[0]["quantity"]
        return jsonify(
            {
                "message": f"The total value of {product_name} is:",
                "total": total,
            }
        )
    return jsonify({"message": "Product not found"})

if __name__ == "__main__":
    app.run(debug=True)
