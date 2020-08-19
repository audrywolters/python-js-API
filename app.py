from flask import Flask, request
app = Flask(__name__)

# landing route
@app.route('/')
def index():
    return 'Oooh Hellooooooo'

# a route with a name
@app.route('/greet')
def say_hello():
    return 'Server says Relax'

# route accepts and prints a variable
@app.route('/user/<username>')
def show_user( username ):
    #return that user!
    return 'Username: %s' % username

#test a POST!
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return 'GET and show a login page'
    elif request.method == 'POST':
        return 'POST and show a login page'

# delete
@app.route('/user/<userID>', methods=['DELETE'])
def remove_user( userID ):
    return 'deleted user %s' % userID

