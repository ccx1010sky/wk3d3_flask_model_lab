from app import app
from flask import render_template
from models.order_lsit import orders

@app.route("/orders")
def index():
    return render_template("index.html",title = "orders",orders = orders)

