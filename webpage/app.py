from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
app = Flask("__name__", static_url_path='')
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
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
