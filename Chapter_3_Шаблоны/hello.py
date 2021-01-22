from flask import Flask
from flask.etx.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return "<h1>Hello World !</h1>"


@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
