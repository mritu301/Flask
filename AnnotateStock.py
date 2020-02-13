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
    #array = request.get_array(field_name='file')
    #print(len(array))
    #print(array[1])
    aspects = []
    aspectList = []
    directory = os.fsencode('Files/')
    print(directory)
    filename = os.fsdecode(os.listdir(directory)[0])
    print(filename)
    print(os.path.join(directory, os.listdir(directory)[0]))
    print("Test")
    with open(os.path.join(directory, os.listdir(directory)[0])) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            aspectList.append( line.strip())
            line = fp.readline()
            cnt += 1

    print("Test end")
    print(aspectList)
    return 0
    #return excel.make_response_from_array(array, "csv", file_name="export_data")


# insert database related code here
if __name__ == "__main__":
    excel.init_excel(app)
    app.run()