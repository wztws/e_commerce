import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200

def test_login(client):
    r = client.get('/login')
    assert r.status_code == 200

def test_register(client):
    r = client.get('/register')
    assert r.status_code == 200

def test_product(client):
    r = client.get('/product')
    assert r.status_code == 200

def test_cart(client):
    r = client.get('/cart')
    assert r.status_code == 302  # 未登录状态下重定向

def test_order(client):
    r = client.get('/order')
    assert r.status_code == 302  # 未登录状态下重定向

def test_message(client):
    r = client.get('/message')
    assert r.status_code == 200

def test_api_login(client):
    r = client.post('/api/login', data={'email': '1@qq.com', 'password': '123'})
    assert r.status_code == 400  # 登录失败

def test_api_logout(client):
    r = client.post('/api/logout')
    assert r.status_code == 400  # 未登录状态下调用

def test_api_register(client):
    r = client.post('/api/register', data={'email': '1@qq.com', 'name': 'zhangsan', 'password': '123'})
    assert r.status_code == 400  # 邮箱已被注册

def test_api_addcart(client):
    r = client.post('/api/addcart', data={'itemid': 1, 'count': 2})
    assert r.status_code == 400  # 未登录状态下调用

def test_api_cart(client):
    r = client.get('/api/cart')
    assert r.status_code == 400  # 未登录状态下调用

def test_404(client):
    r = client.get('/404')
    assert r.status_code == 302  # 重定向到首页