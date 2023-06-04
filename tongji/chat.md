以下是我的html商品展示部分的代码product.html的部分代码，我想要为“加入购物车”的按钮添加功能，将当前的商品信息加入表cart中，使其可以在cart.html界面上显示，同时product.js中关于addcart()的实现和flask后端app.py部分代码也附上，请问该怎么实现呢？
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SWJTU商城</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/common.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/product.css') }}">
    <script src="{{ url_for('static', filename='js/ajax.js') }}"></script>
    <script src="{{ url_for('static', filename='js/product.js') }}"></script>
</head>
<body>
    <div class="app">
        <div class="product-name">
            <div class="product-nav">
                <div class="container">
                    <h2>{{product.name}}</h2>
                    <div class="nav">
                        <a href="#buy" onclick="buy()">立即购买</a>
                        <span class="sep">|</span>
                        <a href="#desc">商品概述</a>
                        <span class="sep">|</span>
                        <a href="#argu">商品参数</a>
                        <!-- <span class="sep">|</span>
                        <a href="#review">商品评价</a> -->
                    </div>
                </div>
            </div>
        </div>
        <div id="desc" class="detail">
            <div class="container">
                <div class="detail-img">
                    <div class="img-img">
                        {% for slide in product.slides %}
                        <div class="img-slide">
                            <img src="{{ url_for('static', filename='image/'+slide.url) }}" alt="">
                        </div>
                        {% endfor %}
                    </div>
                    <div class="img-pagination">
                        {% for slide in product.slides %}
                        <span class="pagination-bullet"></span>
                        {% endfor %}
                    </div>
                    <div class="img-button-prev"></div>
                    <div class="img-button-next"></div>
                </div>
                <div class="detail-right">
                    <h2 class="detail-header">{{product.name}}</h2>
                    <p class="detail-desp">{{product.desc}}</p>
                    <div class="detail-price">
                        <span>{{product.price}}元</span>
                    </div>
                    <div class="line"></div>
                    <div class="detail-num">

                    </div>
                    <div class="detail-total">
                        <ul class="total-list">
                            {% for subitem in [product] %}
                            <li class="total-item">
                                <span class="item-name">{{subitem.name}}</span>
                                <span class="item-price">{{subitem.price}}</span>
                            </li>
                            {% endfor %}
                        </ul>
                        <div class="total-price">总计：{{product.price}}元</div>
                    </div>
                    <div class="detail-button">
                        <div class="detail-addcart"><a href="javascript:void(0);" onclick="addcart()">加入购物车</a>
                            <script>
                            </script>
                        </div>
                        <div class="detail-buynow">
                            <a href="javascript:void(0);" onclick="buy()">立即购买</a>
                            <script>
                                function analy() {
                                    fetch('/buy')
                                }
                            </script>
                            </div>
                        <div class="detail-message">
                            <a href="{{ url_for('message') }}" onclick="message()">私信商家</a></div>
                        <div class="detail-eval">
                            <a href="javascript:void(0);" onclick="eval()">评价商品</a></div>
                    </div>
                </div>
            </div>
        </div>
        <div id="argu" class="product-detail">
            {% for image in product.images %}
            <div class="detail-item">
                <img src="{{ url_for('static', filename='image/'+image.url) }}" alt="">
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
```
```js
function addcart() {
    ajax({
        type: "POST",
        url: "/api/addcart",
        data: {
            itemid: window.location.href.split('/').pop(),
            count: 1
        },
        success(res) {
            window.location.reload();
        },
        fail(err) {
            window.location.href = err.location;
        }
    })
}
```
```python
import os
import json
import random
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
    product['images'] = [{'url': item.image}, {'url': item.image}, {'url': item.image}]
    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]

    return render_template('product.html',
                           user=user,
                           product=product,
                           headerlist=headerlist)
@app.route('/api/cart')
def api_cart():
    if 'iduser' not in session:
        return jsonify({'status': 'error'}), 400
    cart = Cart.query.filter(User.iduser == session['iduser']).all()
    return jsonify({'status': 'ok', 'data': cart})

```
