from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    gender = RadioField("Gender:", choices=[("F", "Female"), ("M", "Male")])
    stem_classifier = RadioField("STEM Classifier:", choices=[("S","STEM"), ("N","Non-STEM")])
    intl = RadioField("International or Domestic:", choices=[("I", "International"), ("D", "Domestic")])
    UNIV101 = RadioField("UNIV101 Indicator:", choices=[("A", "Attended"), ("D", "Did not attend")])
    ENGL109 = RadioField("ENGL109 Indicator:", choices=[("A", "Attended"), ("D", "Did not attend")])
    salary = StringField('Annual Salary')
    submit = SubmitField('Calculate Cluster')
