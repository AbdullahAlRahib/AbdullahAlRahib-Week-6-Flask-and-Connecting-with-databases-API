from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello_world1")
def hello_world1():
    return "<p>Hello, World 1 !</p>"

@app.route("/hello_world2")
def hello_world2():
    return "<p>Hello, World 2 !</p>"

@app.route("/test")
def test():
    a = 5+6
    return "This is my function to run the app {}".format(a)

@app.route("/test2/test2")
def test2():
    data = request.args.get('x')
    return "<h4>This is my input from  my url {}</h4>".format(data)



if __name__ == "__main__":
    app.run(debug=True)