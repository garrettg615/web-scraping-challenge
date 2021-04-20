from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import scrape_mars

# config Flask
app = Flask(__name__)

# establish connections to pymongo database



# create route for homepage
@app.route('/')
def homepage():
    title = 'Exploring Mars'
    
    return render_template('index.html', title=title)

# create page to scrape data
@app.route('/scrape')
def scrape_mars():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)