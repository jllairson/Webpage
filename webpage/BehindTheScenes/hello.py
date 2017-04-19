from flask import Flask
from flask import render_template
app = Flask("MyWebsite")
 
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template("index.html")


app.run()


