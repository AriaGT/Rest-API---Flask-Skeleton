from flask import Blueprint, jsonify, request
import random

from database.products import products

productsRouter = Blueprint('publicationsRouter', __name__)

@productsRouter.route('/api/v1/products/')
def getProducts():
  return jsonify({
    "message": "Products List",
    "products": products
  })

@productsRouter.route('/api/v1/products/', methods=['POST'])
def addProduct():
  newProduct = {
    "id": request.json["id"],
    "name": request.json["name"],
    "price": request.json["price"],
    "quantity": request.json["quantity"]
  }
  products.append(newProduct)
  return jsonify({
    "message": "Success, Product Added!",
    "products": products
  })

@productsRouter.route('/api/v1/products/random/')
def getRandomProduct():
  randomIndex = random.randint(1, len(products)) - 1
  return jsonify({
    "product": products[randomIndex]
  })

@productsRouter.route('/api/v1/products/<int:product_id>/')
def getProduct(product_id):
  productFound = [product for product in products if product['id'] == product_id]
  if (len(productFound) > 0):
    return jsonify({
      "message": "Success!",
      "product": productFound[0]
    })
  return jsonify({
    "message": "Error, product not found"
  }), 404

@productsRouter.route('/api/v1/products/<int:product_id>/', methods=['PUT'])
def editProduct(product_id):
  productFound = [product for product in products if product['id'] == product_id]
  if (len(productFound) > 0):
    productFound[0]["name"] = request.json["name"]
    productFound[0]["price"] = request.json["price"]
    productFound[0]["quantity"] = request.json["quantity"]
    return jsonify({
      "message": "Success, Product Updated",
      "newProductData": productFound
    })
  return jsonify({
    "message": "Error, product not found."
  })

@productsRouter.route('/api/v1/products/<int:product_id>/', methods=['DELETE'])
def removeProduct(product_id):
  productFound = [product for product in products if product['id'] == product_id]
  if (len(productFound) > 0):
    products.remove(productFound[0])
    return jsonify({
    "message": "Success, product removed.",
    "products": products
  })
  return jsonify({
    "message": "Error, product not found."
  }), 404