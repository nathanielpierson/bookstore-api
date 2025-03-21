from flask import Flask, request
import db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

#index for books
@app.route('/books.json')
def books_index():
    return db.books_all()

#create for books
@app.route("/books.json", methods=["POST"])
def create():
    title = request.form.get("title")
    print(request.form)
    author = request.form.get("author")
    price = request.form.get("price")
    stock = request.form.get("stock")
    return db.books_create(title, author, price, stock)

#index for customers
@app.route('/customers.json')
def customers_index():
    return db.customers_all()

#index for orders
@app.route('/orders.json')
def orders_index():
    return db.orders_all()
