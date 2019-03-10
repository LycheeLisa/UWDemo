from flask import Flask, render_template, flash, redirect, request
from app import app
from app.forms import InfoForm
from flask_bootstrap import Bootstrap
from random import randrange #for testing- TO BE DELETED
import csv, sys



app = Flask(__name__, template_folder='templates/DevFolio')
Bootstrap(app)
app.config['SECRET_KEY'] = 'asecretkey'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    inputs = []
    clusterNum = 6
    clusterInfo = []
    clusterName = "No Name"
    clusterSpider = "static/images/problem.png"
    clusterStats =  "static/images/problem.png"


    if form.validate_on_submit():
        inputs.extend((form.year.data, form.program.data, form.salaryFirst.data, form.salaryLast.data, form.firstEval.data,
        form.lastEval.data, form.coopTerms.data, form.uniAvg.data, form.hsAvg.data, form.uniYears.data, form.gender.data, form.stem.data))
        inputs = toInt(inputs)
        flash('Data entered {}'.format(inputs))
        clusterNum = puesdoModel(inputs) #returns a number between 1 and 6
        clusterInfo = gatherFiles(clusterNum)
        clusterName = clusterInfo[1]
        clusterSpider = "static/images/" + clusterInfo[2]
        clusterStats = "static/images/" + clusterInfo[3]
<<<<<<< HEAD
    return render_template("index.html", title = 'IWD 2019',form=form, input=inputs, clusterNum=clusterNum,
=======
    return render_template("index.html", title = 'UWaterloo Demo',form=form, input=inputs, clusterNum=clusterNum,
>>>>>>> c01621e50bf76e1fab33bf1a971c2d5090f549f9
    clusterName = clusterName, clusterSpider = clusterSpider, clusterStats = clusterStats)

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
