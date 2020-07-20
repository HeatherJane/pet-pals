# import necessary libraries
from sqlalchemy import func
from sqlalchemy import create_engine
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
app = Flask(__name__)
# @TODO: Setup your database here
engine = create_engine('sqlite:///db/pets.sqlite')
@app.route("/")
def home():
    return render_template("index.html")
# @TODO: Create a route "/send" that handles both GET and POST requests
@app.route("/send", methods=["GET", "POST"])
def send():
    conn = engine.connect()
    if request.method == "POST":
        petname = request.form["petName"]
        pettype = request.form["petType"]
        petage = request.form["petAge"]
        pet_df = pd.DataFrame({
            'Pet_name': [petname],
            'Pet_Type': [pettype],
            'Pet_Age' : [petage]
        })
        pet_df.to_sql('petdata', con=conn, if_exists='append', index=False)
        return "Thanks for the form data!"
    return render_template("form.html")
# If the request method is POST, save the form data to the database
# Otherwise, return "form.html"
# @TODO: Create an API route "/api/pals" to return data to plot
@app.route("/api/pals")
def list_pets():
    conn = engine.connect()
    pets_df = pd.read_sql('SELECT * FROM petdata', con=conn)
    pets_json = pets_df.to_json(orient='records')
    conn.close()
    return pets_json
@app.route("/api/pals-summary")
def summary_pets():
    conn = engine.connect()
    pets_df1 = pd.read_sql('select pet_type, count(pet_type) as count_pets from petdata group by pet_type', con=conn)
    pets_json1 = pets_df1.to_json(orient='records')
    conn.close()
    return pets_json1
if __name__ == "__main__":
    app.run(debug=True)