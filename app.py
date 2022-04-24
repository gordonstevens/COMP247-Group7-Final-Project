from flask import Flask, render_template, request
import model
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/sub', methods=["GET","POST"])
def submit():
    if request.method == "POST":
        d = request.form
        data = pd.DataFrame(data=d, index=[0])
        print(data)
        result = model.predictor(data)
        
    return render_template("sub.html", n = d, mResult = result[0])


# ImmutableMultiDict([('Cost_of_Bike', '234'), ('Bike_Model', ''), ('Bike_Make', ''), ('Primary_Offence', ''), 
# ('Bike_Colour', ''), ('Occurrence_DayOfYear', '246'), ('Report_DayOfYear', '247'), ('Location_Type', ''), ('Bike_Speed', ''), 
# ('NeighbourhoodName', '')])

if __name__ == "__main__":
	app.run(debug = True)