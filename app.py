# import necessary libraries
from flask import Flask, render_template, redirect
# from flask_pymongo import PyMongo
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# create instance of Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)
mongo.db.items.drop()


# setup mongo connection
#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(conn)

# connect to mongo db and collection
#db = client.mars_db
#collection = db.items


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():
    

    # Find data
    # items = list(db.collection.find())
    

    items = list(mongo.db.items.find())
    print("what is this??", items)

    # return template and data
    return render_template("index.html", items=items)


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():
    results = []
    mongo.db.items.drop()
    

    # Run scraped functions
    items = scrape_mars.scrape()

    # Store results into a dictionary
    for item in items:
        print('items in scrape are',item)
        results.append({"title": item["title"], "img_url": item["img_url"]})
        # Insert result into database
    mongo.db.items.insert_many(results)

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
