from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

class InfoForm(FlaskForm):
    gender = RadioField("Gender:", choices=[("0", "Female"), ("1", "Male")])
    stem_classifier = RadioField("STEM Classifier:", choices=[("0","STEM"), ("1","Non-STEM")])
    intl = RadioField("International or Domestic:", choices=[("0", "International"), ("1", "Domestic")])
    UNIV101 = RadioField("UNIV101 Indicator:", choices=[("0", "Attended"), ("1", "Did not attend")])
    ENGL109 = RadioField("ENGL109 Indicator:", choices=[("0", "Attended"), ("1", "Did not attend")])
    salary = StringField('Annual Salary')
    submit = SubmitField('Calculate Cluster')
    myField = SelectField(u'Field name', choices = [("0","Hello"),(1,"Baby")])
