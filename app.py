from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server is Worksies'

@app.route('/greet')
def say_hello():
    return 'Server says Relax'