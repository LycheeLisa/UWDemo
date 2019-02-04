from flask import Flask, render_template, flash, redirect, request
from app import app
from app.forms import InfoForm
from flask_bootstrap import Bootstrap
from random import randrange #for testing- TO BE DELETED
import csv, sys



app = Flask(__name__, template_folder='templates')
# bootstrap_app = Bootstrap(app)
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
        # 12 inputs
        inputs.extend((form.gender.data, form.stem_classifier.data, form.intl.data, form.UNIV101.data, form.ENGL109.data, form.salary.data, form.myField.data))
        inputs = toInt(inputs)
        flash('Data entered {}'.format(inputs))
        clusterNum = puesdoModel(inputs) #returns a number between 1 and 6
        clusterInfo = gatherFiles(clusterNum)
        clusterName = clusterInfo[1]
        clusterSpider = "static/images/" + clusterInfo[2]
        clusterStats = "static/images/" + clusterInfo[3]
    return render_template("homepage.html", title = 'UWaterloo Demo',form=form, input=inputs, clusterNum=clusterNum,
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
