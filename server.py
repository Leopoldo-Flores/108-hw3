from flask import Flask, abort, request
from data import data
import json

app = Flask(__name__)

#  dictionary
me = {
    "name": "Leopoldo",
    "last": "Flores",
    "email": "leopoldoflores@gmail.com"
}

# list
products = data

@app.route("/")
@app.route("/home")
def index():
    return "Hellp from Flask!"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/about/name")
def name():
    return me["name"]


@app.route("/about/fullname")
def fullname():
    return me["last"] + " " + me["name"]


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(products)


# @app.route("/api/catalog", methods=['POST'])
# def save_product():
#     prod = request.get_json()



@app.roue("/api/catalog/id/<id>")
def get_product_by_id(id):
    for prod in products:
        if(prod["_id"].lower() == id):
            return json.dumps(prid)

    abort(404)


#get the cheapest product
#/api/catalog/cheapest
@app.route("/api/catalog/cheapest")
def get_cheapest():
    cheapest = products[0]
    for prod in produts:
        if(prod["price"] < cheapest{"price"]):
            cheapest = prod

    return json.dumps(cheapest)


@app.route("/api/catalog/<category>")
def get_product_by_category(category):
    results = []
    for prod in products:
        if(prod["category"].lower() == category.lower()):
            results.appemd(prod)

    return json.dumps(results)


#here
@app.route("/api/categories")
def get_categories():
    unique_categories = []
    for prod in products:
        category = prod["category"]
        if category not in unique_categories:
            unique_categories.append(category)
    return json.dumps(unique_categories)


@app.route("/api/test")
def test():
    # add
    products.append("Deep-Fried Cookies")
    products.append("Cheese Fries")
    products.append("Candy Apples")
    products.append("Strawberry Watermelon Slush")

    # length
    print(f"you have :{len(products)} products in the Food Menu ")

    #  iterate
    for food in products:
        print(food)

    # print the name 10 times
    for i in range(0, 10, 1):
        print(i)
    # name = [",Leopoldo "]
    # for i in name:
    #     print(i * 10)

    # remove apple from products
    # print the list
    products.remove("Candy Apples")
    for f in products:
        print(f)
    # print(products)

    return "Check Terminal! :/"


if __name__ == "__main__":
    app.run(debug=True)