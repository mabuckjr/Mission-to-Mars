# Importing tools/dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["Mongo_URI"] = "mongodb://localhost:271017/mars_app"
mongo = PyMongo (app)

# Define the route for the html page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Define the route for the button feature
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code = 302)

# Tell it to run
if __name__ == "__main__":
   app.run()