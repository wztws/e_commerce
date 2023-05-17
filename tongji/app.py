import os
import json
import random
from datetime import datetime, timedelta

from flask import Flask, request, render_template, session, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'  # 设置session加密的密钥
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/webhw'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    password = db.Column(db.String(45), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def header(self):
        header = {}
        header['name'] = self.name
        cartcount = Cart.query.filter(Cart.iduser == self.iduser).count()
        header['cartcount'] = cartcount
        return header


class Item(db.Model):
    __tablename__ = 'item'
    iditem = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)

    price = db.Column(db.DECIMAL(5), nullable=True)
    image = db.Column(db.Text)
    desc = db.Column(db.String(45), nullable=True)
    time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class Order(db.Model):
    __tablename__ = 'order'
    idorder = db.Column(db.Integer, primary_key=True)
    iduser = db.Column(db.Integer, db.ForeignKey('user.iduser'))
    iditem = db.Column(db.Integer, db.ForeignKey('item.iditem'))
    item = db.relationship('Item', backref='orders')
    user = db.relationship('User', backref='orders')


class Cart(db.Model):
    __tablename__ = 'cart'
    idorder = db.Column(db.Integer, primary_key=True)
    iduser = db.Column(db.Integer, db.ForeignKey('user.iduser'))
    iditem = db.Column(db.Integer, db.ForeignKey('item.iditem'))
    count = db.Column(db.DECIMAL(2), nullable=True)
    item = db.relationship('Item', backref='carts')
    user = db.relationship('User', backref='carts')


class Image(db.Model):
    __tablename__ = 'image'
    idimage = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=True)
    iditem = db.Column(db.Integer, db.ForeignKey('item.iditem'))
    item = db.relationship('Item', backref='images')


class OrderItem(db.Model):
    '''订单项'''
    __tablename__ = "order_item"
    _id = db.Column(db.Integer, primary_key=True)
    orderid = db.Column(db.Integer, db.ForeignKey("order.idorder", ondelete='cascade'))
    order = db.relationship("Order", backref=db.backref("the_Orderitem"))
    itemid = db.Column(db.Integer, db.ForeignKey("item.iditem"))
    item = db.relationship("Item", backref=db.backref("the_Orderitem"))
    count = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    user = {}
    if 'iduser' in session:
        dbuser = User.query.get(session['iduser'])
        print(dbuser)
        user['name'] = dbuser.name
        cartcount = Cart.query.filter(Cart.iduser == dbuser.iduser).count()
        user['cartcount'] = cartcount

    slides = [{'href': "product.html", 'url': url_for('static', filename="image/banner/01.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/02.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/03.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/04.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/05.png")}]

    list1 = Item.query.limit(8).all()
    print(list1)

    list2 = Item.query.offset(8).limit(10).all()

    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]
   # print(headerlist)
    return render_template('index.html',
                           slides=slides,
                           user=user,
                           list1=list1,
                           list2=list2,
                           headerlist=headerlist)


@app.route('/product')
@app.route('/product/<int:_id>')
def product(_id=0):
    user = {}
    if 'iduser' in session:
        user = User.query.get(session['iduser']).header()
    item = Item.query.filter(Item.iditem == _id).first()
    product = {}
    product['name'] = item.name
    product['desc'] = item.desc
    product['price'] = item.price
    product['slides'] = [{'url': item.image}]
    product['images'] = [{'url': item.image}, {'url': item.image}, {'url': item.image}]


    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]

    return render_template('product.html',
                           user=user,
                           product=product,
                           headerlist=headerlist)


@app.route('/cart')
def cart():
    if 'iduser' not in session:
        return redirect(url_for('login', src=request.url))
    user = User.query.get(session['iduser']).header()
    dbuser = User.query.get(session['iduser'])
    carts = Cart.query.filter(User.iduser == session['iduser']).all()
    return render_template('cart.html',
                           user=user,
                           carts=carts)


@app.route('/order')
def order():
    if 'iduser' not in session:
        return redirect(url_for('login', src=request.url))
    dbuser = User.query.get(session['iduser'])
    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]

    return render_template('order.html', user=dbuser.header(),headerlist=headerlist)


@app.route('/login')
def login():
    return render_template('login.html',
                           src=request.args.get('src', ''))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/message')
def message():
    return render_template('message.html')


@app.route('/api/login', methods=["POST"])
def api_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter(User.email == email).first()
    if user and user.password == password:
        session['iduser'] = user.iduser
        return jsonify({'status': 'ok', 'location': url_for('index')})
    else:
        return jsonify({'status': 'error'}), 400


@app.route('/api/logout', methods=["POST"])
def api_logout():
    if 'iduser' in session:
        session.pop('iduser')
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'}), 400


@app.route('/api/register', methods=["POST"])
def api_register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    if User.query.filter(User.email == email).first():
        return jsonify({'status': '邮箱重复'}), 400
    elif User.query.filter(User.name == name).first():
        return jsonify({'status': '用户名重复'}), 400
    else:
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'ok', 'location': url_for('index')})


@app.route('/api/addcart', methods=["POST"])
def api_addcart():
    if 'iduser' not in session:
        return jsonify({'status': 'error', 'location': url_for('login')}), 400
    itemid = request.form.get('itemid')
    count = request.form.get('count')
    cart = Cart(iduser=session['iduser'], itemid=itemid, count=count)
    db.session.add(cart)
    db.session.commit()
    return jsonify({'status': 'ok'})


@app.route('/api/cart')
def api_cart():
    if 'iduser' not in session:
        return jsonify({'status': 'error'}), 400
    cart = Cart.query.filter(User.iduser == session['iduser']).all()
    return jsonify({'status': 'ok', 'data': cart})


@app.errorhandler(404)
def not_foundPage(error):
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)