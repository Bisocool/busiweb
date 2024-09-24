from flask import Flask, render_template, request, redirect, session
from flask_session import Session

# Initializing app
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# The Portfolio Route
@app.route("/")
def index():
    return render_template("app.html")

# Was in use but now is not because it is unnecessary
@app.route("/display")
def display():
    return render_template("index2.html", name=session.get("name"))