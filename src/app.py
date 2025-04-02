from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("/workspaces/flask-render-integration/models/decision_tree_classifier_default_42.sav", "rb"))

@app.route("/", methods = ["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Obtain values from form
        val1 = int(request.form["val1"])
        val2 = int(request.form["val2"])
        val3 = int(request.form["val3"])
        
        data = [[val1, val2, val3]]
        prediction = int(model.predict(data)[0])
    
    return render_template("index.html", prediction = prediction)