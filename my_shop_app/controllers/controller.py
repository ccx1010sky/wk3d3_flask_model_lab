from app import app
from flask import render_template
from models.order_lsit import orders

@app.route("/")

def index():
    return render_template("index.html",title = "Food shop")

# 
@app.route("/orders")
def order():
    return render_template("order.html",title = "orders",orders = orders)






