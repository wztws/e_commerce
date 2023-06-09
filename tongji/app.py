import os
import json
import random
from sqlalchemy import func, or_
from datetime import datetime, timedelta
from flask import Flask, request, render_template, session, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from collections import defaultdict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'w522328z'  # 设置session加密的密钥
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:w522328z@localhost:3306/webhw'
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True, autoincrement=True, default=1)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    password = db.Column(db.String(45), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    auth=db.Column(db.Integer)   
    def header(self):
        header = {}
        header['iduser'] = self.iduser
        header['name'] = self.name
        header['email'] = self.email
        header['phone'] = self.phone
        header['password'] = self.password
        header['create_time'] = self.create_time
        if self.auth==1:
            header['auth'] = '顾客'
        elif self.auth==2:
            header['auth'] = '商家'
        cartcount = Cart.query.filter(Cart.iduser == self.iduser).count()
        header['cartcount'] = cartcount
        return header
    def get_auth(self):
        return self.auth
class Merchant(db.Model):
    __tablename__ = 'merchant'
    id = db.Column(db.Integer)
    iditem = db.Column(db.Integer)
    image = db.Column(db.Text)
    image2 = db.Column(db.Text)
    image3 = db.Column(db.Text)
    image4 = db.Column(db.Text)
    species = db.Column(db.Integer)
    store = db.Column(db.Integer)
    price = db.Column(db.DECIMAL(5, 2))
    desc = db.Column(db.String(45))
    creatime = db.Column(db.DateTime, primary_key=True, default=datetime.now)
    name = db.Column(db.String(45), nullable=True)

    def __init__(self, id, iditem, image, image2, image3, image4, species, store, price, desc, name):
        self.id = id,
        self.iditem = iditem
        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.species = species
        self.store = store
        self.price = price
        self.desc = desc
        self.name = name
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
    def __init__(self, iditem, name, price, image, image2, image3, image4, species, desc):
        self.iditem=iditem
        self.name = name
        self.price = price
        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.species = species
        self.desc = desc

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
        #dbuser = User.query.get(session['iduser'])
       # print(dbuser)
        dbuser = db.session.get(User, session['iduser'])
        user['name'] = dbuser.name
        cartcount = Cart.query.filter(Cart.iduser == dbuser.iduser).count()
        user['cartcount'] = cartcount
        user['auth'] = dbuser.get_auth()

    slides = [{'href': "product.html", 'url': url_for('static', filename="image/banner/宣传图1.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/宣传图2.jpg")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/宣传图3.jpg")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/宣传图4.jpg")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/宣传图5.jpg")}]

    list1 = Item.query.limit(12).all()
    print(list1)

    list2 = Item.query.offset(15).limit(14).all()

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
    carts = Cart.query.join(User).filter(User.name == user['name']).all()
    print("用户id: "+str(user))
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

@app.route('/add_item')
def add_item():
    user = User.query.get(session['iduser']).header()
    return render_template('add_item.html', user=user)


@app.route('/manager_product')
def manager_product():
    user = db.session.get(User, session['iduser'])
    user_name = user.name if user is not None else None
    user = User.query.filter_by(name=user_name).first()
    merchants = Merchant.query.filter_by(id=user.iduser).all()
    return render_template('manager_product.html', merchants=merchants, user=user)

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
    auth = request.form.get('auth')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    max_iduser = db.session.query(func.max(User.iduser)).scalar()
    if max_iduser is None:
        max_iduser = 0
    if User.query.filter(User.email == email).first():
        return jsonify({'status': '邮箱重复'}), 400
    elif User.query.filter(User.name == name).first():
        return jsonify({'status': '用户名重复'}), 400
    else:
        user = User(iduser=max_iduser+1, name=name, email=email, password=password, auth=auth)
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
        cart = Cart(idorder=max_idorder + 1,  iduser=userid, iditem=iditem, count=1)
        
        db.session.add(cart)
        db.session.commit()

        response = jsonify({'message': '添加成功'})
        response.status_code = 200

        return response
   else:
        return jsonify({'status': 'error', 'message': '产品未找到！'})
   

@app.route('/del_cart', methods=['POST'])
def del_cart():
    data = request.json

    item_name = data.get('name')
    item_price = data.get('price')
    order_id = data.get('idorder')
    print(item_name)
    print(item_price)
    print(order_id)
    Cart.query.filter_by(idorder=order_id).delete()
    db.session.commit()
    # 在这里进行进一步的处理，例如保存到数据库或执行其他操作
    return 'Success'  # 返回适当的响应

@app.route('/del_merchant', methods=['POST'])
def del_merchant():
    data = request.get_json()
    item_id = data.get('id')
    # 在这里进行处理，例如删除对应的商户或执行其他操作
    print(item_id)
    merchant = Merchant.query.filter_by(iditem=item_id).first()
    item = Item.query.filter_by(iditem=item_id).first()

    # 删除商户和商品
    if merchant:
        db.session.delete(merchant)
    if item:
        db.session.delete(item)

    db.session.commit()
    return 'Success'


@app.route('/submit', methods=['POST']) #添加商品
def additem():
    user_name = User.query.get(session['iduser']).name
    user = User.query.filter_by(name=user_name).first()
    print(user.iduser)
    item_name = request.form.get('item-name')
    item_species = request.form.get('item-species')
    item_stock = request.form.get('item-stock')
    item_price = request.form.get('item-price')
    item_description = request.form.get('item-description')
    max_iditem = db.session.query(func.max(Item.iditem)).scalar()
    # 处理上传的图片
    image1 = request.files['image1']
    image2 = request.files['image2']
    image3 = request.files['image3']
    image4 = request.files['image4']
    # 保存图片到指定路径
    image1.save(os.path.join(app.root_path, 'static/image', image1.filename))
    image2.save(os.path.join(app.root_path, 'static/image', image2.filename))
    image3.save(os.path.join(app.root_path, 'static/image', image3.filename))
    image4.save(os.path.join(app.root_path, 'static/image', image4.filename))
    merchant = Merchant(
        id=user.iduser,
        iditem=max_iditem + 1,  # 根据需要设置iditem
        image=image1.filename,
        image2=image2.filename,
        image3=image3.filename,
        image4=image4.filename,
        species=item_species,
        store=item_stock,
        price=item_price,
        desc=item_description,
        name=item_name
    )
    db.session.add(merchant)
    db.session.commit()
    item = Item(
        iditem=max_iditem + 1,  # 根据需要设置iditem
        name=item_name,
        price=item_price,
        image=image1.filename,
        image2=image2.filename,
        image3=image3.filename,
        image4=image4.filename,
        species=item_species,
        desc=item_description,
    )
    db.session.add(item)
    db.session.commit()
    response = jsonify({'message': '添加成功'})
    response.status_code = 200
    return response

   


@app.errorhandler(404)
def not_foundPage(error):
    return redirect(url_for('index'))

# 搜索页面
@app.route('/search')
def search():
    if 'iduser' not in session:
        return redirect(url_for('login', src=request.url))
    user = User.query.get(session['iduser']).header()
    carts = Cart.query.join(User).filter(User.name == user['name']).all()
    print("用户id: "+str(user))
    total_price = 0
    for cart in carts:
        total_price += cart.item.price * cart.count
    query = request.args.get('query')
    if not query:
        # 没有输入关键字，显示搜索页面
        return render_template('search.html')
    else:
        # 根据关键字进行商品搜索
        items = Item.query.filter(Item.name.like(f'%{query}%')).all()
        # 显示搜索结果页面
        return render_template('search.html', query=query, items=items, carts=carts,user=user, total_price=total_price)

# 个人中心页面
@app.route('/center')
def center():
    if 'iduser' not in session:
        return redirect(url_for('login', src=request.url))
    user = User.query.get(session['iduser']).header()
    carts = Cart.query.join(User).filter(User.name == user['name']).all()
    print("用户id: "+str(user))
    total_price = 0
    for cart in carts:
        total_price += cart.item.price * cart.count
    print(user)
    return render_template('center.html',user=user)


# 获取指定时间范围内的消费金额和类别信息
def get_data(start, end):
    # 查询数据
    transactions = db.session.query(Transaction.amount, Transaction.category, Transaction.date).\
        filter(Transaction.date >= start, Transaction.date <= end).all()

    # 按照时间单位统计消费金额
    unit = request.args.get('unit', 'day')
    if unit == 'day':
        date_format = '%Y-%m-%d'
        delta = timedelta(days=1)
    elif unit == 'week':
        date_format = '%Y-%u'
        delta = timedelta(weeks=1)
    elif unit == 'month':
        date_format = '%Y-%m'
        delta = timedelta(days=30)
    elif unit == 'year':
        date_format = '%Y'
        delta = timedelta(days=365)
    else:
        date_format = '%Y-%m-%d'
        delta = timedelta(days=1)

    date_dict = defaultdict(int)
    for row in transactions:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        date_key = datetime.strftime(date, date_format)
        date_dict[date_key] += row[0]

    # 构造返回数据
    chart1_categories = []
    chart1_values = []
    for key, value in sorted(date_dict.items()):
        chart1_categories.append(key)
        chart1_values.append(value)

    category_dict = defaultdict(int)
    for row in transactions:
        category_dict[row[1]] += row[0]

    chart2_data = []
    for key, value in sorted(category_dict.items(), key=lambda x: x[1], reverse=True):
        chart2_data.append({'name': key, 'value': value})

    # 关闭数据库连接
    db.session.close()

    return {'chart1': {'categories': chart1_categories, 'values': chart1_values}, 'chart2': chart2_data}

# 返回数据接口
@app.route('/stats')
def stats():
    start = request.args.get('start')
    end = request.args.get('end')
    data = get_data(start, end)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)