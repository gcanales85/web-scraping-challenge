from flask import Flask, render_template,redirect, request, jsonify
from flask_pymong import PyMongo
#From the separate python file in this directory, we'll import the code that is used to scrape mars
import scrape_mars


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# identify the collection and drop any existing data for this demonstration
mars_info = mongo.db.mars_info
mars_info.drop()

# Render the index.html page with any craigslist listings in our database. 
# If there are no listings, the table will be empty.
@app.route("/")
def index():
    mars_results = mars_info.find()
    return render_template("index.html", mars_results=mars_results)


# route triggering the scrapping function
@app.route("/scrape")
def scraper():

        # perform the scrape using our search term 
        # scrape_mars.scrape() is a custom function that we've defined in the scrape_mars.py file within this directory
         mars_data = scrape_mars.scrape()

        # Insert the results that we receive from the web scrape
        mars_info.insert_many(mars_data)

    # Use Flask's redirect function to send us to a different route once this task has completed.
    return 'Finished!'


if __name__ == "__main__":
    app.run(debug=True)