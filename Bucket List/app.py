from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("your url")
db = client.dbsparta
# db.test01.insert_one({"msg": "checking bucket list"})


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {"_id": False}))

    return jsonify({"msg": bucket_list})


@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form["bucket_give"]

    count = db.bucket.count_documents({})
    print(count)
    num = count + 1

    doc = {"num": num, "bucket": bucket_receive, "done": 0}

    db.bucket.insert_one(doc)
    return jsonify({"msg": "data saved!"})


@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form["num_give"]
    db.bucket.update_one({"num": int(num_receive)}, {"$set": {"done": 1}})
    return jsonify({"msg": "Update done!"})


@app.route("/delete", methods=["POST"])
def delete_bucket():
    num_receive = request.form["num_give"]
    db.bucket.delete_one({"num": int(num_receive)})
    return jsonify({"msg": "delete done!"})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
