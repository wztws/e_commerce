import requests

def test_index():
    r = requests.get('http://127.0.0.1:5000/')
    assert r.status_code == 200

def test_login():
    r = requests.get('http://127.0.0.1:5000/login')
    assert r.status_code == 200

def test_register():
    r = requests.get('http://127.0.0.1:5000/register')
    assert r.status_code == 200

def test_product():
    r = requests.get('http://127.0.0.1:5000/product')
    assert r.status_code == 200

def test_api_login():
    r = requests.post('http://127.0.0.1:5000/api/login', data={'email': '1@qq.com', 'password': '123'})
    assert r.status_code == 400

def test_api_logout():
    r = requests.post('http://127.0.0.1:5000/api/logout')
    assert r.status_code == 400

def test_api_register():
    r = requests.post('http://127.0.0.1:5000/api/register', data={'email': '1@qq.com', 'name': 'zhangsan', 'password': '123'})
    assert r.status_code == 400

def test_api_addcart():
    r = requests.post('http://127.0.0.1:5000/api/addcart', data={'itemid': 1, 'count': 2})
    assert r.status_code == 400

def test_api_cart():
    r = requests.get('http://127.0.0.1:5000/api/cart')
    assert r.status_code == 400