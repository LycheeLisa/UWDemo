from flask import Flask, render_template, flash, redirect, request
from app import app
from app.forms import InfoForm
from flask_bootstrap import Bootstrap
from random import randrange #for testing- TO BE DELETED
import csv, sys
from app.clusters import Cluster
from ClusterModel import master



app = Flask(__name__, template_folder='templates')
Bootstrap(app)
app.config['SECRET_KEY'] = 'asecretkey'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    myCluster = Cluster(5)
    inputs = []
    clusterNum = 6
    clusterName = myCluster.getInfo()[1]
    clusterSpider = "static/images/problem.png"
    clusterStats =  "static/images/problem.png"


    if form.validate():
        inputs.extend((form.year.data, form.program.data, form.salaryFirst.data, form.salaryLast.data, form.firstEval.data,
        form.lastEval.data, form.coopTerms.data, form.uniAvg.data, form.hsAvg.data, form.uniYears.data, form.gender.data, form.stem.data))
        inputs = toInt(inputs)
        clusterNum = master(inputs) #returns a number between 1 and 6
        myCluster.update(clusterNum)
    return render_template("indexTEST.html", title='UWaterloo Demo', myCluster=myCluster, form=form, inputs=inputs)

@app.route('/about', methods=['GET'])
def about():
    return render_template("aboutproject.html", title= "About This Project")


@app.route('/result', methods=['GET', 'POST'])

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

# fake model function
def puesdoModel(list):
    x = randrange(6)
    x = x+1
    flash(x)
    return x
# def results(inputs):
#     results = request.form
#     print results
if __name__ == "__main__":
    app.run(debug=True, port=9999)
