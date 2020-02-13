# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:29:51 2020

@author: MJ
"""

from flask import Flask, request, jsonify, render_template, session
import flask_excel as excel
from flask_session import Session
import os
import pandas as pd

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

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
    #filename = os.fsdecode(os.listdir(directory)[0])

    with open(os.path.join(directory, os.listdir(directory)[0])) as fp:
        line = fp.readline()
        while line:
            aspects.append( line.strip())
            line = fp.readline()
            
    columns = ["Sentences"] + aspects
    session["transcript"]=array
    session["columns"]=columns
    return render_template("annotate.html", content=columns, file=array)
    #return excel.make_response_from_array(array, "csv", file_name="export_data")

@app.route("/download", methods=['POST'])
def download_file():
    print("inside download_file")
    checkbox_aspect = request.form.getlist("aspect")
    print(checkbox_aspect)
    aspect = session["columns"]
    sent = session["transcript"]
    #print(aspect)
    #print(sent[0][0])
    df = pd.DataFrame(columns = aspect)
    #print(df)
    #print(list(data.columns.values))
    
    print(type(aspect))
    print(type(sent))
    print(aspect[0])
    print(aspect[0] == "Sentences")
    for row in range(1, len(sent)+1):
        #print(sent[row-1][0])
        for column in range(1,len(aspect)+1):
            #print("inside 2nd loop")
            temp_aspect = "aspect_"+str(row)+"_"+str(column)
            #print(temp_aspect)
            #if temp_aspect in list(checkbox_aspect):
            #    print(temp_aspect)
            print("row = ", row-1, "column = ", column)
            if column == 1:
                print("first column 00 = ", sent[row-1][0])
                df.loc[row-1, aspect[column-1]] = sent[row-1][0]
            elif temp_aspect in list(checkbox_aspect):
                print("2nd if ", temp_aspect, " = ", str(1))
                df.loc[row-1, aspect[column-1]] = str(1)
            else:
                print("Last else ")
                df.loc[row-1, aspect[column-1]] = str(0)
            #print("row = ", row, "column = ", column)
            #print("aspect_"+str(row)+"_"+str(column))
                
    print(df.head())
    print("End Logic!!!")
    df.to_csv(r"Annotated_Transcript.csv",index = None, header=True)
    return render_template("thankyou.html")


# insert database related code here
if __name__ == "__main__":
    excel.init_excel(app)
    app.run()