from flask import Flask, request, render_template, redirect, session, url_for
from flask_cors import CORS
from flask_mysqldb import MySQL
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
CORS(app)

# 生成一个16字节的随机十六进制字符串作为密钥
app.secret_key = secrets.token_hex(16)

# 配置数据库连接信息
mysql_connect_url = 'mysql+mysqlconnector://root:123456@localhost:3306/e_commerce?auth_plugin=mysql_native_password'
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_connect_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 初始化数据库连接对象
db = SQLAlchemy(app)

# 定义用户表类
class User(db.Model):
    __tablename__ = 'user'

    Uid = db.Column(db.String(45), primary_key=True)
    Uname = db.Column(db.String(45), unique=True, nullable=False)
    Upassword = db.Column(db.String(45), nullable=False)
    Uemail = db.Column(db.String(45))
    Uaddress = db.Column(db.String(125))
    Uphone = db.Column(db.String(45))
    Ulevel = db.Column(db.String(45))
    Umoney = db.Column(db.String(45))
    Ugender = db.Column(db.String(45))
    Uimage = db.Column(db.LargeBinary)
    reg_time = db.Column(db.String(45), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    create_time = db.Column(db.String(45), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    update_time = db.Column(db.String(45), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        user = db.session.query(User).filter_by(Uname=username).first()
        print(user)
        if user:
            # 登录成功，将用户信息保存到session中
            session['user_id'] = user.Uid
            session['user_name'] = user.Uname
            # 跳转到其他页面
            return redirect(url_for('index'))
        else:
            # 用户名或密码错误，返回到登录页面重新输入
            return render_template('login.html', error='用户名或密码错误')
    else:
        # GET请求，返回登录页面
        return render_template('login.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        email = request.form.get('email')
        address = request.form.get('address')
        phone = request.form.get('phone')
        now = datetime.now()
        id_str = now.strftime('%Y%m%d%H%M%S%f')[:-3]  # 格式化当前时间并去除毫秒
        id_num = int(id_str.replace(':', '').replace('-', '').replace(' ', ''))  # 将时间字符串转为数字

        user = User(Uid=id_num, Uname=nickname, Upassword=password, Uemail=email, Uaddress=address, Uphone=phone)
        db.session.add(user)
        db.session.commit()

        # 注册成功，跳转到登录页面
        return redirect(url_for('login'))
    else:
        # GET请求，返回注册页面
        return render_template('register.html')

@app.route("/order", methods=["POST", "GET"])
def order():
    return render_template('order.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)