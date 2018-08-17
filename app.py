"""
Flask app module

@date: 8/17/2018
@author: Larry Shi
"""

# general imports
from flask import Flask, render_template

# initialize app
app = Flask(__name__)


# page route
@app.route('/')
def index():
    return render_template('index.html')


# run server
if __name__ == '__main__':
    app.run()
