# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 00:10:49 2020

@author: MJ
"""

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template("home.html", content=["Tim", "Joe", "MJ"], r=2)

@app.route('/test')
def test():
    return render_template("new.html", content=["Tim", "Joe", "MJ"], r=2)

if __name__ == '__main__':
    app.run()