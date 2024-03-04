from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("your url")
db = client.dbsparta
# db.test01.insert_one({"msg": "hello24-02-2024"})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/mars", methods=["GET"])
def mars_get():
    orders_list = list(db.orders.find({}, {"_id": False}))
    return jsonify({"orders": orders_list})


@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form["name_give"]
    address_receive = request.form["address_give"]
    size_receive = request.form["size_give"]
    doc = {"name": name_receive, "address": address_receive, "size": size_receive}
    db.orders.insert_one(doc)
    return jsonify({"msg": "POST request done!"})


# if __name__ == "__main__":
#     app.run("0.0.0.0", port=5000, debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
