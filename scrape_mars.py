import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo

def scrape_mars_info():
    """Define function to scrape all websites and get information about Mars"""

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    db = client.mars_db
    collection = db.mars_data

    collection.drop()
    

    # Scrape for Mars headline and paragraph

    executable_path = {'executable_path':'/Users/garrettgomez/.wdm/drivers/chromedriver/mac64/89.0.4389.23/chromedriver'}
    browser = Browser('chrome',**executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_mars = soup.find('div', class_='content_title').text
    para_mars = soup.find('div', class_='article_teaser_body').text

    mars_dict = {
        'title':title_mars,
        'descript':para_mars
        }
    collection.insert_one(mars_dict)

    browser.quit()

    # Scrape for Mars Featured image

    executable_path = {'executable_path':'/Users/garrettgomez/.wdm/drivers/chromedriver/mac64/89.0.4389.23/chromedriver'}
    browser = Browser('chrome',**executable_path, headless=False)

    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)

    time.sleep(1)

    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')


    mars_image = soup2.find_all('img')[1]["src"]
    mars_image_path = url2 + mars_image
    
    mars_dict = {'img_url':mars_image_path}
    
    collection.insert_one(mars_dict)
    browser.quit()

    # Use Pandas to scrape for Mars Fact Table
    url3 = 'https://galaxyfacts-mars.com'

    tables = pd.read_html(url3)
    mars_facts = tables[1]
    mars_facts.columns = ['Attribute','Spec']
    
    ## Write table to html
    table_file = open('./templates/mars_table.html','w')
    table_file.write(mars_facts.to_html())
    table_file.close()
    

    # Scrape for Mars Hemisphere Images and Name

    executable_path = {'executable_path':'/Users/garrettgomez/.wdm/drivers/chromedriver/mac64/89.0.4389.23/chromedriver'}
    browser = Browser('chrome',**executable_path, headless=False)
    url4 = 'https://marshemispheres.com/'
    

    browser.visit(url4)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='description')

    for result in results:
        title_text = result.find('a').h3.text
        browser.find_by_text(title_text).first.click()

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        image_info = soup.find('div', class_='description').a['href']
        image_url = url4+image_info
        mars_dict = {
            'title':title_text,
            'image_url':image_url
        }
        
        collection.insert_one(mars_dict)
        browser.back()

    browser.quit()
    
    
    return 'mars info scraped'

