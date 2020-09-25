from dotenv import load_dotenv
from os import getenv
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# Load environment variables
load_dotenv()

# Create an instance of Flask
app = Flask(__name__)

# Get the connection string for the database
app.config['MONGO_URI'] = getenv('MONGO_URI', '')

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)

if __name__ == "__main__":
    app.run(debug=True)