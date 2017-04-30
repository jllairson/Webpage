from flask import Flask
from flask import render_template
from flask import request
app = Flask("__name__")
@app.route('/')
def hello_world():
    return 'hello world!'
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/intro')
def intro():
    return "This is the Intro page"
if __name__ == '__main__':
    app.run(debug=True)	
