from flask import Flask

app = Flask(__name__)


@app.route("/")
def my_func():
    return "hello world"

@app.route("/welcome")
def my_func_new():
    return "welcome"


if __name__ == '__main__':
    app.run(debug=True)
