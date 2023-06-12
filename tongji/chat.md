您好，以下这段flask代码中，我想从Order表中获取所有的iduser与user['name']相同的数据信息,该怎么修改呢


```python
class User(db.Model):
    __tablename__ = 'user'
    iduser = db.Column(db.Integer, primary_key=True, autoincrement=True, default=1)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=True)
    phone = db.Column(db.String(45), nullable=True)
    password = db.Column(db.String(45), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    auth=db.Column(db.Integer)
    address=db.Column(db.Text)
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
class Order(db.Model):
    __tablename__ = 'order'
    idorder = db.Column(db.Integer, autoincrement=True, default=1)
    iduser = db.Column(db.Text)
    idmerchant = db.Column(db.Text)
    iditem = db.Column(db.Text)
    ifecho = db.Column(db.Integer)
    price = db.Column(db.Text)
    total = db.Column(db.Integer)
    item_num = db.Column(db.Text)
    time = db.Column(db.DateTime, primary_key=True, default=datetime.now)
    def __init__(self, iduser, idmerchant, iditem, ifecho, price, total, item_num):
        self.iduser = iduser
        self.idmerchant = idmerchant
        self.iditem = iditem
        self.ifecho = ifecho
        self.price = price
        self.total = total
        self.item_num  =item_num


@app.route('/order')
def order():
    if 'iduser' not in session:
        return redirect(url_for('login', src=request.url))
    user = User.query.get(session['iduser']).header()
    print(user['name'])
    return render_template('order.html', user=user)

```