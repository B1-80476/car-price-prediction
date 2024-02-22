from flask import Flask, request, render_template

import pickle
import sklearn
app = Flask(__name__)
# load the model
with open('C:\\Users\\admin\\Desktop\\ML project\\Ml-model-deploy\\RandomForest001.pkl', 'rb') as file:
    model = pickle.load(file)

# with open('/home/ubuntu/RandomForest002.pkl', 'rb') as file:
#     model = pickle.load(file)

# create a flask application

# /home/ubuntu

@app.route("/", methods=["GET"])
def root():
    # read the file contents and send them to client
    return render_template('pric.html')


@app.route("/classify", methods=["POST"])
def classify():
    # get the values entered by user
    print(request.form)

    year = float(request.form.get("year"))
    manufacturer = (request.form.get("manufacturer"))
    cylinders = (request.form.get("cylinders"))
    fuel = (request.form.get("fuel"))
    odometer = float(request.form.get("odometer"))
    drive = (request.form.get("drive"))



    price = model.predict([[year, manufacturer, cylinders, fuel, odometer, drive]])

    # price = model.predict([[2016,3,3,2,150000,1]])

    # return f"price:{price[0]}"
    return render_template("pric.html", result=price[0])

def perform_prediction(year, manufacturer, cylinders, fuel, odometer, drive):
    result = f'Predicted result for {year}, {manufacturer}, {cylinders}, {fuel}, {odometer}, {drive}'
    return result

# start the application
app.run(host="0.0.0.0", port=8000, debug=True)