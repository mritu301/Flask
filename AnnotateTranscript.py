# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:55:39 2020

@author: MJ
"""

from flask import Flask, request, jsonify, render_template, session, redirect, url_for
import flask_excel as excel
from flask_session import Session
import os
import pandas as pd

app = Flask(__name__)

# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route("/thankyou", methods=['GET'])
def thankyou():
    return render_template("thankyou.html")

@app.route("/error", methods=['GET'])
def error():
    return render_template("error.html")

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #return jsonify({"result": request.get_array(field_name='file')})
        return render_template("error.html")
    return render_template("upload.html")


@app.route("/export", methods=['POST'])
def export_records():
    print("inside export")
    try:
        array = request.get_array(field_name='file')
    except:
        print("An exception occurred")
        return redirect(url_for("error"))
        
    aspects = []
    
    directory = os.fsencode('Files/')

    with open(os.path.join(directory, os.listdir(directory)[0])) as fp:
        line = fp.readline()
        while line:
            aspects.append( line.strip())
            line = fp.readline()
            
    columns = ["Sentences"] + aspects
    session["transcript"]=array
    session["columns"]=columns
    return render_template("annotate.html", content=columns, file=array)

@app.route("/download", methods=['GET', 'POST'])
def download_file():
    print("inside download_file")
    if request.method == 'POST':
        print("Post Call...")
        checkbox_aspect = request.form.getlist("aspect")
    
        aspect = session["columns"]
        sent = session["transcript"]

        df = pd.DataFrame(columns = aspect)
    
        for row in range(1, len(sent)+1):
            for column in range(1,len(aspect)+1):
                temp_aspect = "aspect_"+str(row)+"_"+str(column)
                if column == 1:
                    df.loc[row-1, aspect[column-1]] = sent[row-1][0]
                elif temp_aspect in list(checkbox_aspect):
                    df.loc[row-1, aspect[column-1]] = str(1)
                else:
                    df.loc[row-1, aspect[column-1]] = str(0)
                
        df.to_csv(r"Annotated_Transcript.csv",index = None, header=True)
        print("end...")
        return redirect(url_for("thankyou"))
    else:
        return redirect(url_for("error"))

# run the app
if __name__ == "__main__":
    excel.init_excel(app)
    app.run()