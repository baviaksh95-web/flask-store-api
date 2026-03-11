from flask import Flask,jsonify
from models import db,User,Product,Order
import config 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Flask Storage API"

#add user
@app.route('/add_user')
def add_user():
    user = User(name="Anish", email = "anish123@gmail.com")
    db.session.add(user)
    db.session.commit()
    return "User Added"

#add product
@app.route('/add_product')
def add_product():
    p1 = Product(name="Laptop", price=50000)
    p2 = Product(name="Mobile", price=20000)
    p3 = Product(name="iPad", price=65000)

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()

    return "Products Added" 

@app.route('/products')
def get_products():
    products = Product.query.all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price
        })

    return jsonify(result)
#view users
@app.route('/users')
def get_users():
    users = User.query.all()

    result = []
    for u in users:
        result.append({
            "id" : u.id,
            "name" : u.name,
            "email" : u.email
        })
    return jsonify(result)

@app.route('/add_order')
def add_order():
    order = Order(user_id = 1)
    db.session.add(order)
    db.session.commit()
    return "Order Added"


if __name__ == "__main__":
    app.run(debug = True)
