# flask-rest boilerplate
from flask import Flask, request

app = Flask(__name__)


app.route("/")
def hello():
    return "Free Tier Limit Exceded!"

