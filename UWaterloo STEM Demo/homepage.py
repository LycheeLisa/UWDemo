from flask import Flask, render_template, flash, redirect, request
from app import app
from app.forms import InfoForm
from flask_bootstrap import Bootstrap


app = Flask(__name__, template_folder='templates')
# bootstrap_app = Bootstrap(app)
app.config['SECRET_KEY'] = 'asecretkey'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    inputs = []
    if form.validate_on_submit():
        inputs.extend((form.gender.data, form.stem_classifier.data, form.intl.data, form.UNIV101.data, form.ENGL109.data, form.salary.data))
        flash('Data entered {}'.format(inputs))
    return render_template("homepage.html", title = 'Machine Learning Demo',form=form, input=inputs)
    
@app.route('/about', methods=['GET'])
def about():
    return render_template("aboutproject.html", title= "About This Project")

@app.route('/result', methods=['GET', 'POST'])
def results():
    results = request.form
    print results
if __name__ == "__main__":
    app.run(debug=True, port=9999)
