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


@app.route("/orders/list1")
def list1():
    return render_template("list1.html",title = "list1", orders = orders)
@app.route("/orders/list2")
def list2():
    return render_template("list2.html",title = "list2", orders = orders)
@app.route("/orders/list3")
def list3():
    return render_template("list3.html",title = "list3", orders = orders)





