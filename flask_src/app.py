from flask import Flask, redirect, url_for, render_template, request, jsonify
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://bacon:tamushamu2001@cluster0.3ksm9.mongodb.net/howdy_hack_2020?retryWrites=true&w=majority")
db = cluster["howdy_hack_2020"]
collection = db["howdy_hack_2020"]

# inserts a post/ document into the mongodb collection

@app.route("/", methods=["POST", "GET"])
def breach():
    if request.method == "POST":
        email = request.form["email"]
        phone = request.form["phone"]
        # Make the id iterate
        count = len(db.tamu_hack_2020.distinct("_id")) + 1
        post = {"email": email, "phone": phone}
        collection.insert_one(post)
        # Run Amari's python file
        return redirect(url_for("user", usr=user))
    else:
        return render_template("breach.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
