
import uuid

from flask import Flask, jsonify, request
from products import products
from helpers import get_items_with_name

app = Flask(__name__)

#Main Route
@app.route('/')
def welcome():
    """Turn an object into a json to web browser"""
    return jsonify({"message": "Welcome to my first CRUD"})

#Routes    
#Existing products
@app.route('/products', methods=['GET'])
def getProducts():
    """Asign to products property"""
    return jsonify({"products": products, "message": "Product's list" }) 

#Specific product
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    """Find the product and validate if product exist un products. 
       If exist,return the first value from productFound's list"""
    productFound = get_items_with_name(product_name)
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0]}) 
    return jsonify({"message": "Product not found"})

#Create product
@app.route('/products', methods = ['POST'])
def addProduct():
    """Create a new product: Using Postman POST request"""
    new_product = {
        "id": str(uuid.uuid4()),
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

#Edit Product
@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    """Update product properties, name, price or quantity: Using Postman PUT request"""
    body = request.json
    productFound = get_items_with_name(product_name)
    if (len(productFound) > 0):
        productFound[0]["name"] = body["name"]
        productFound[0]["price"] = body["price"]
        productFound[0]["quantity"] = body["quantity"]
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})

  #debe ser posible update solo un campo  

#Delete product
@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
    """Delete a product from its name: Using Postman DELETE"""
    productFound = get_items_with_name(product_name)
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "Product not found"})

#Total value of products in the store
@app.route('/products/sum-stock')
def sumStock():
    """Calculate the total value of each element and returns the sum of them"""
    # name = [product['name'] for product in products]
    # value_per_product = ([product["price"] * product["quantity"] for product in products])
    # total = dict(zip(name,value_per_product))

    total = {product['name']: product["price"] * product["quantity"] for product in products}
    return jsonify({"message": "The total value of your stock is:", "total": total})

if __name__ == '__main__':
    app.run(debug=True) 