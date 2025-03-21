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
def books_create():
    title = request.form.get("title")
    author = request.form.get("author")
    price = request.form.get("price")
    stock = request.form.get("stock")
    return db.books_create(title, author, price, stock)

#show for books
@app.route("/books/<id>.json")
def show(id):
    return db.books_find_by_id(id)

#index for customers
@app.route('/customers.json')
def customers_index():
    return db.customers_all()

#create for customers
@app.route("/customers.json", methods=["POST"])
def customers_create():
    name = request.form.get("name")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")
    return db.customers_create(name, email, phone_number)

#index for orders
@app.route('/orders.json')
def orders_index():
    return db.orders_all()
