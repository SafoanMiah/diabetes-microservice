from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/altair")
def altair():
    return render_template("altair.html")


if __name__ == '__main__':
    app.run()