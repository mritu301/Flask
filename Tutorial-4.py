# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 00:10:49 2020

@author: MJ
"""

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    print("home")
    return render_template("home.html", content=["Tim", "Joe", "MJ"], r=2)

@app.route('/login', methods=["POST", "GET"])
def login():
    print("login")
    if request.method == "POST":
        user = request.form["name"]
        print(user, "POSt")
        return redirect(url_for("user", usr=user))
    else:
        print("GET")
        return render_template("login.html", content=["Tim", "Joe", "MJ"], r=2)

@app.route("/<usr>")
def user(usr):
    print("user")
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run()