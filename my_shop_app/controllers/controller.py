from app import app
from flask import render_template
from models.order_lsit import orders



# Function name can be anything,
#  assign "Food shop" to title variable in the index.html
# assign orders object to orders variable in every html file.
@app.route("/")

def index():
    return render_template("index.html",title = "Food shop1")

@app.route("/orders")
def order():
    return render_template("order.html",title = "orders",orders = orders)

# listindex type is string, listindex is parameter
# assign orders[int(listindex)] to list_item variable,and pass to list_item argument.
@app.route("/orders/<listindex>")
def list1(listindex):
    list_item = orders[int(listindex)]
    return render_template("list1.html",title = "list1", list_item =list_item)





