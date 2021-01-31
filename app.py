
# Import flask
from flask import Flask

# create an app, being sure to pass __name__
app = Flask(__name__)

# define what to do when user hits the index route
@app.route('/')
def hello_world():
    return 'Hello world'
    
    