from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# config Flask
app = Flask(__name__)

# establish connections to pymongo database
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")



# create route for homepage
@app.route('/')
def homepage():
    news = mongo.db.collection.find_one()
    
    return render_template('index.html', headlines=news)

# create page to scrape data
@app.route('/scrape')
def scrape_mars_redirect():
    mars_info = scrape_mars.scrape_mars_info()
    mongo.db.collection.update({},mars_info,upsert=True)
    print('it scraped')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)