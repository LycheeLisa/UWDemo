from flask import Flask, render_template, flash, redirect, request
from app import app
from app.forms import InfoForm
from flask_bootstrap import Bootstrap
import csv, sys
from app.clusters import Cluster
from ClusterModel import master
import json


app = Flask(__name__, template_folder='templates')
Bootstrap(app)
app.config['SECRET_KEY'] = 'asecretkey'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    return render_template("index.html", title='UWaterloo Demo', form=form)


@app.route('/formsubmit', methods=['GET', 'POST'])
def formsubmit():

    inputs = request.form['data']
    inputs = inputs.strip('"').split("&")
    formval={};

    for i in range(len(inputs)-1):
        formval[inputs[i+1].split("=")[0]] = int(inputs[i+1].split("=")[1])

    modelList = [formval["year"], formval["program"], formval["salaryFirst"], formval["salaryLast"], formval["firstEval"],
    formval["lastEval"], formval["coopTerms"], formval["uniAvg"], formval["hsAvg"], formval["uniYears"], formval["gender"], formval["stem"]]

    clusterNum = master(modelList)
    myCluster = Cluster(clusterNum)

    return render_template("profile.html", title='UWaterloo Demo', myCluster=myCluster)

@app.route('/clusterview', methods=['GET', 'POST'])
def clusterview():
    data = request.form['data']
    clusterNum = int(data.strip('"'))
    myCluster = Cluster(clusterNum)
    return render_template("profile.html", title='UWaterloo Demo', myCluster=myCluster)

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
    app.run(debug=True, port=9999)
