import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_1 = pickle.load(open("models/model.pkl", "rb"))
model_2 = pickle.load(open("models/model_.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/page1.html', methods=['GET', 'POST'])
def predict_earthquake():
    if request.method == 'POST':
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model_1.predict(features)
        return render_template("page1.html", prediction_text="Magnitude = {}".format(prediction))
    else:
        return render_template("page1.html")
    
@app.route('/page2.html', methods=['GET', 'POST'])
def predict_damage():
    if request.method == 'POST':
        struct_type = float(request.form['structType'])
        year_built = float(request.form['yearBuilt'])
        num_stories = float(request.form['numStories'])
        distance = float(request.form['distance'])
        magnitude = float(request.form['magnitude'])
        features = [np.array([struct_type, year_built, num_stories, distance])]
        prediction = model_2.predict(features)
        if magnitude > 5:
            prediction += 0.85*np.log10(magnitude - 4)
        elif magnitude < 5:
            prediction -= 0.2*prediction
        
        return render_template("page2.html", prediction_text_="MeanDamage = {}".format(prediction))
    else:
        return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug=True)