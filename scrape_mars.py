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
    
    browser.quit()

    # Use Pandas to scrape for Mars Fact Table
    url3 = 'https://galaxyfacts-mars.com'

    tables = pd.read_html(url3)
    mars_facts = tables[1]
    mars_facts.columns = ['Attribute','Spec']
    mars_table = mars_facts.to_html()
    
    ## Write table to html
    table_file = open('mars_table.html','w')
    table_file.write(mars_table)
    table_file.close()

    # Scrape for Mars Hemisphere Images and Name

    executable_path = {'executable_path':'/Users/garrettgomez/.wdm/drivers/chromedriver/mac64/89.0.4389.23/chromedriver'}
    browser = Browser('chrome',**executable_path, headless=False)
    url4 = 'https://marshemispheres.com/'
    
    mars_hem = []
    mars_imgs = []

    browser.visit(url4)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='description')

    for result in results:
        title_text = result.find('a').h3.text
        mars_hem.append(title_text)
        browser.find_by_text(title_text).first.click()

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        image_info = soup.find('div', class_="downloads").ul.li.a['href']
        image_url = url4+image_info
        mars_imgs.append(image_url)
        
        browser.back()

    browser.quit()
    
    
    mars_dict = {
        'headline':title_mars,
        'news':para_mars,
        'featured_img':mars_image_path,
        'mars_hems':mars_hem,
        'mars_hem_imgs':mars_imgs,
        'mars_table':mars_table
    }
    
    return mars_dict

