from app import app

@app.route('/')
def home():
    user = {"username": "Lisa"}
    form = InfoForm()
    return render_template("homepage.html", title = 'UWaterloo Demo', user=user, form=form)
