from flask import Flask, render_template, flash, redirect, request
from app import app
from app.forms import InfoForm
from flask_bootstrap import Bootstrap
import csv, sys
from app.clusters import Cluster
from ClusterModel import master
import time, datetime
import json
import pandas as pd


app = Flask(__name__, template_folder='templates')
Bootstrap(app)
app.config['SECRET_KEY'] = 'asecretkey'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    return render_template("index.html", title='UWaterloo Demo', form=form)

#Render profile based on Model inputs, store model inputs and cluster and generate summary graph.
@app.route('/formsubmit', methods=['GET', 'POST'])
def formsubmit():

    #form values selected from posted json data
    inputs = request.form['data']
    inputs = inputs.strip('"').split("&")
    formval={};

    #populate dictionary with form data
    for i in range(len(inputs)-1):
        formval[inputs[i+1].split("=")[0]] = int(inputs[i+1].split("=")[1])

    modelList = [formval["year"], formval["program"], formval["salaryFirst"], formval["salaryLast"], formval["firstEval"],
    formval["lastEval"], formval["coopTerms"], formval["uniAvg"], formval["hsAvg"], formval["uniYears"], formval["gender"], formval["stem"]]

    #run the data through the model "master"
    clusterNum = master(modelList)
    #shift the cluster value based on gender to generate the right gender profile
    profileNum = modelList[10]*6 + clusterNum

    #generate the cluster object with the associated cluster values
    myCluster = Cluster(profileNum)
    #write the model results to a table
    saveResults(clusterNum, modelList)
    #generate the summary results from the table
    graphData = clusterGraph()

    total = sum(graphData)

    return render_template("profile.html", title='UWaterloo Demo', myCluster=myCluster, clusterGraph=graphData, total= total)

#Render profile based on Cluster selection, store model inputs and cluster and generate summary graph.
@app.route('/clusterview', methods=['GET', 'POST'])
def clusterview():
    #cluster profile selected from posted json data
    data = request.form['data']
    clusterNum = int(data.strip('"'))

    #generate the cluster object with the associated cluster values
    myCluster = Cluster(clusterNum)

    #generate the summary results from the table
    graphData = clusterGraph()
    total = sum(graphData)

    return render_template("profile.html", title='UWaterloo Demo', myCluster=myCluster, clusterGraph=graphData, total= total)
#lookup actual value using numeric values
def lookupValue(modelList):
    data = pd.read_csv("static/data/lookup_matrix.txt", names=list(range(13)), delimiter="\t", encoding="cp1252", header=None)
    formInputs = [(data.iat[(modelList[i])+1,(i+1)]) for i in range(len(modelList))]
    return formInputs

#write data results to a table
def saveResults(cluster, data):
    curTime =  time.time()
    timestamp =  datetime.datetime.fromtimestamp(curTime).strftime('%Y-%m-%d %H:%M:%S')
    dataEntry = [timestamp, cluster] + lookupValue(data)
    print(dataEntry)
    with open('static/data/Model_Results.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(dataEntry)
    return dataEntry

#generate summary data from table
def clusterGraph():
    modelData = pd.read_csv("static/data/Model_Results.csv")
    counts = modelData.Cluster.value_counts()

    keys = pd.DataFrame(counts).reset_index()['index'].astype(int).tolist()
    data = counts.tolist()

    clusterGraph = [0,0,0,0,0,0]

    for i in range(len(keys)):
        val = int(keys[i])
        clusterGraph[val-1] += data[i]

    return clusterGraph

#gather graphics file names based on cluster
def gatherFiles (clusterNum):
    f = open("static/data/graphics_files.csv", "rb")
    reader = csv.reader(f, delimiter = ",")
    data = list(reader)
    data = data[clusterNum]
    f.close()
    return data

#covnert string list to int list
def toInt(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])
    return strList

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
