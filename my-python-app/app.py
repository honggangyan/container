from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World! Nice to meet you!"


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
