import pytest
from flask import session

from app import app, db, User, Cart, Item

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_login(client):
    # 创建测试用户
    user = User(name='TestUser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()

    # 登录
    response = client.post('/api/login', data={'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200
    assert 'iduser' in session

def test_add_to_cart(client):
    # 创建测试用户和商品
    user = User(name='TestUser', email='test@example.com', password='password')
    item = Item(name='TestItem', price=10.0)
    db.session.add_all([user, item])
    db.session.commit()

    # 模拟登录
    with client.session_transaction() as sess:
        sess['iduser'] = user.iduser

    # 添加商品到购物车
    response = client.post('/addcart', data={'itemid': item.iditem, 'count': 1})
    assert response.status_code == 200

    # 验证购物车是否成功添加
    cart = Cart.query.filter_by(iduser=user.iduser).first()
    assert cart is not None
    assert cart.item == item
    assert cart.count == 1

def test_cart(client):
    # 创建测试用户和购物车商品
    user = User(name='TestUser', email='test@example.com', password='password')
    item = Item(name='TestItem', price=10.0)
    cart = Cart(user=user, item=item, count=2)
    db.session.add_all([user, item, cart])
    db.session.commit()

    # 模拟登录
    with client.session_transaction() as sess:
        sess['iduser'] = user.iduser

    # 检查购物车页面是否返回正确
    response = client.get('/cart')
    assert response.status_code == 200
    assert b'TestItem' in response.data

def test_register(client):
    # 注册新用户
    response = client.post('/api/register', data={'name': 'NewUser', 'email': 'newuser@example.com', 'password': 'password'})
    assert response.status_code == 200

    # 验证新用户是否成功注册
    user = User.query.filter_by(email='newuser@example.com').first()
    assert user is not None

def test_logout(client):
    # 创建测试用户
    user = User(name='TestUser', email='test@example.com', password='password')
    db.session.add(user)
    db.session.commit()

    # 模拟登录
    with client.session_transaction() as sess:
        sess['iduser'] = user.iduser

    # 注销
    response = client.post('/api/logout')
    assert response.status_code == 200
    assert 'iduser' not in session

