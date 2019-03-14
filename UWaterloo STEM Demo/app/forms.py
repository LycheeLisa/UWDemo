from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
import csv
import numpy as np
import pandas as pd

def gatherOptions (filename):
    data = pd.read_csv(filename, names=list(range(13)))
    # dataTran = data.T
    return data

def createChoices (col,data):
    choices = data.iloc[:,col]
    choices = choices.dropna()
    choices = choices.values[1:]
    choiceList = [ (str(i), choices[i]) for i in range(len(choices))]
    return choiceList

# def formTuple (list)
class InfoForm(FlaskForm):
    optionsFile = "static/data/lookup_matrix.csv"
    formOptions = gatherOptions(optionsFile)
    optionNames = formOptions.iloc[0,:]
    year =  SelectField(optionNames[1], choices = createChoices(1,formOptions))
    program = SelectField(optionNames[2], choices = createChoices(2,formOptions))
    salaryFirst = SelectField(optionNames[3], choices = createChoices(3,formOptions))
    salaryLast = SelectField(optionNames[4], choices = createChoices(4,formOptions))
    firstEval = SelectField(optionNames[5], choices = createChoices(5,formOptions))
    lastEval = SelectField(optionNames[6], choices = createChoices(6,formOptions))
    coopTerms = SelectField(optionNames[7], choices = createChoices(7,formOptions))
    uniAvg = SelectField(optionNames[8], choices = createChoices(8,formOptions))
    hsAvg = SelectField(optionNames[9], choices = createChoices(9,formOptions))
    uniYears = SelectField(optionNames[10], choices = createChoices(10,formOptions))
    gender = SelectField(optionNames[11], choices = createChoices(11,formOptions))
    stem = SelectField(optionNames[12], choices = createChoices(12,formOptions))
