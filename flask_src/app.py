from flask import Flask, redirect, url_for, render_template, request, jsonify
import pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient 
from update import update
app = Flask(__name__)

# inserts a post/ document into the mongodb collection

@app.route("/", methods=["POST", "GET"])
def breach():
    if request.method == "POST":
        email = request.form["email"]
        phone = request.form["phone"]

        # Run e-mail and text script
        update(email, phone)

        return render_template("success.html")
    else:
        return render_template("breach.html")

if __name__ == "__main__":
    app.run(debug=True)
