from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
def say_hello():
    return 'Hello!!!!!'

@app.route('/hello/<username>')
def hello_user(username):
    return f'Hello {username}!'

@app.route('/error')
def raise_error():
    raise RuntimeError('Just for fun')

@app.route('/task/', methods=['GET', 'POST'])
def task():
    return 'Task view'
