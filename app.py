from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, You Could you please subscribe!</p> <br /> <h2>EEX Tv </h2>"
