from flask import Flask, render_template, request, redirect
import time
import os
import compilationMessage
import pandas as pd
import numpy as np
import logic

app = Flask(__name__,static_url_path='', static_folder='frontend/static',template_folder='frontend/templates')
port = int(os.environ.get("PORT", 5000))
compilationsBool = True
messagetype = ""
data = []
l = ""

@app.route('/')
@app.route('/index')
def index():
    global data
    global l
    memoryTree = []
    memorryData = pd.read_csv("memory.csv") 
    memorryData = memorryData.replace(np.nan, '', regex=True)
    accumulators = 0

    for i in range(len(memorryData)):
        if(memorryData['Data'][i]!=""):
            memoryTree.append([memorryData['Address'][i],int(memorryData['Data'][i])])
        else:
            memoryTree.append([memorryData['Address'][i],memorryData['Data'][i]])
    if(len(data)!=0):
        if("7001" not in data):
            compilationsBool = False
            messagetype = compilationMessage.no7001
        else:
            logicData = logic.mainF(data)
            if(logicData[1]>=1):
                compilationsBool = False
                messagetype = compilationMessage.wrongAddress
            else:
                accumulators = logicData[0]
                compilationsBool = True
                messagetype = compilationMessage.PerfectCompilations
        if(compilationsBool==True):
            return render_template('index.html',default_code=l,compilations=messagetype,compileColor="#22a022",memoryDict=memoryTree,accumulator=accumulators,outputSteps=''.join(logicData[2]))
        else:
            return render_template('index.html',default_code=l,compilations=messagetype,compileColor="#ff0000",memoryDict=memoryTree)
    return render_template('index.html',default_code=l,memoryDict=memoryTree)

@app.route('/run', methods=['POST'])
def run():
    global data
    global l
    data = request.form['codes']
    l = data
    data = data.split("\r")
    data = [data[i].replace('\n','') for i in range(len(data))]
    return redirect('/')

@app.route('/memory', methods=['POST'])
def memory():
    Mdata = request.form['memoryLoc']
    Mdata = Mdata.split(",")
    print(Mdata)
    memorryData = pd.read_csv("memory.csv") 
    memorryData = memorryData.replace(np.nan, '', regex=True)
    memorryData['Data'][int(Mdata[0].replace(",",""))%200] = Mdata[1]
    memorryData.to_csv("memory.csv",index=False)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)