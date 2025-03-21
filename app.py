from flask import Flask, request
from flask_cors import CORS
import db

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)



# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})







@app.route('/')
def hello():
    return 'Hello, World!'

#index for books
@app.route('/books.json')
def books_index():
    return db.books_all()

#index for customers
@app.route('/customers.json')
def customers_index():
    return db.customers_all()

#index for orders
@app.route('/orders.json')
def orders_index():
    return db.orders_all()
