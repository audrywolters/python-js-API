from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Oooh Hellooooooo'

@app.route('/greet')
def say_hello():
    return 'Server says Relax'

@app.route('/user/<username>')
def show_user( username ):
    #return that user!
    return 'Username: %s' % username
    