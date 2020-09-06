from flask import Flask, redirect, url_for, render_template, request, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://bacon:tamushamu2001@cluster0.3ksm9.mongodb.net/howdy-hack-2020?retryWrites=true&w=majority")
db = cluster["howdy-hack-2020"]
collection = db["howdy-hack-2020"]

post = {"_id":00, "email": "test@gmail.com", "phone": 1234567890}

# inserts a post/ document into the mongodb collection
collection.insert_one(post)

@app.route("/", methods=["POST", "SGET"])
def breach():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("breach.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
