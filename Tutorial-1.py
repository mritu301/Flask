# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:55:14 2020

@author: MJ
"""

from flask import Flask, redirect, url_for

app = Flask(__name__)
admin = False

@app.route('/')
def home():
    return "Hey there! <h1> This is MJ Page </h1>"

@app.route('/<name>')
def user(name):
    return f"Hello <h1> {name} </h1>"

@app.route("/admin/")
def admin():
    if admin :
        return redirect(url_for("home"))
    else :
        return redirect(url_for("user", name="Admin!!!"))

if __name__ == '__main__':
    app.run()