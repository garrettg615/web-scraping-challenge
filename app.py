from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# config Flask
app = Flask(__name__)

# establish connections to pymongo database
mongo = PyMongo(app=app, uri="mongodb://localhost:27017/mars_db")



# create route for homepage
@app.route('/')
def homepage():
    mars = mongo.db.mars_data.find_one()
    for k,v in mars.items():
        if k == 'mars_hems':
            hem_1 = v[0]
            hem_2 = v[1]
            hem_3 = v[2]
            hem_4 = v[3]

        elif k == 'mars_hem_imgs':
            img_1 = str(v[0])
            img_2 = str(v[1])
            img_3 = str(v[2])
            img_4 = str(v[3])

    return render_template('index.html', mars=mars,hem1=hem_1,hem2=hem_2,hem3=hem_3,hem4=hem_4,img1=img_1,img2=img_2,img3=img_3,img4=img_4)

# # create page to scrape data
@app.route('/scrape')
def scrape_mars_redirect():
    mars_info = scrape_mars.scrape_mars_info()
    mongo.db.mars_data.update({},mars_info,upsert=True)
    print('it scraped')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)