import os
import json
import random
from sqlalchemy import func
from datetime import datetime, timedelta
from flask import Flask, request, render_template, session, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'w522328z'  # 设置session加密的密钥
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:w522328z@localhost:3306/webhw'
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    password = db.Column(db.String(45), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    auth=db.Column(db.Integer)   
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
    image2 = db.Column(db.Text)
    image3 = db.Column(db.Text)
    image4 = db.Column(db.Text)
    species = db.Column(db.Integer)
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
    idorder = db.Column(db.Integer, primary_key=True, autoincrement=True, default=1)
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

    list1 = Item.query.limit(12).all()
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
    img = Image.query.filter(Image.idimage == _id).first()
    product = {}
    product['name'] = item.name
    product['desc'] = item.desc
    product['price'] = item.price
    product['slides'] = [{'url': item.image}]
    product['images'] = [{'url': item.image2}, {'url': item.image3}, {'url': item.image4}]
    #product['images'] = [{'url': img.url}, {'url': img.url}, {'url': img.url}]

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
    carts = Cart.query.filter(User.iduser == session['iduser']).all()
    user = User.query.get(session['iduser']).header()
    total_price = 0
    for cart in carts:
        total_price += cart.item.price * cart.count
    return render_template('cart.html', carts=carts,user=user, total_price=total_price)
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

@app.route('/api/addcart', methods=['POST'])
def api_addcart():
   data = request.json
   user_name = data['user_name']
   product_name = data['product_name']
   print(product_name)
   print(user_name)
     # 查询与产品名称匹配的Item对象
   item = Item.query.filter_by(name=product_name).first()
   user = User.query.filter_by(name=user_name).first()
   if item:
        iditem = item.iditem  # 获取iditem值
        userid = user.iduser
       # iduser = 1  # 假设用户ID为1，根据实际情况获取用户ID
        print(iditem)
        print(userid)
        max_idorder = db.session.query(func.max(Cart.idorder)).scalar()
        if max_idorder is None:
            max_idorder = 0

        # 创建 Cart 对象并将数据存储到数据库中
        cart = Cart(idorder=max_idorder + 1,  iduser=1,iditem=iditem, count=1)
        
        db.session.add(cart)
        db.session.commit()

        return jsonify({'status': 'success', 'message': '成功添加到购物车！'})
   else:
        return jsonify({'status': 'error', 'message': '产品未找到！'})
   

@app.errorhandler(404)
def not_foundPage(error):
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)