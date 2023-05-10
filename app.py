from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template('login.html')

@app.route("/order", methods=["POST", "GET"])
def order():
    return render_template('order.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)