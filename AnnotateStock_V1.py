# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:10:52 2020

@author: MJ
"""

from flask import Flask, request, jsonify, render_template
import flask_excel as excel
import os

app = Flask(__name__)


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='file')})
    return render_template("upload.html")


@app.route("/export", methods=['POST'])
def export_records():
    print("inside export")
    array = request.get_array(field_name='file')
    aspects = []
    
    directory = os.fsencode('Files/')
    filename = os.fsdecode(os.listdir(directory)[0])

    with open(os.path.join(directory, os.listdir(directory)[0])) as fp:
        line = fp.readline()
        while line:
            aspects.append( line.strip())
            line = fp.readline()
            
    columns = ["Sentences"] + aspects
    return render_template("annotate.html", content=columns, file=array)
    #return excel.make_response_from_array(array, "csv", file_name="export_data")


# insert database related code here
if __name__ == "__main__":
    excel.init_excel(app)
    app.run()