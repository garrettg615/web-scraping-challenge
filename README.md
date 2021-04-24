# web-scraping-challenge
Web Scraping Homework

The main application for this assignment is app.py. All contents except the Mars Fact table are rendered from the main application to HTML. You will still find that the information scraped from https://galaxyfacts-mars.com will still be stored in the mongo database. In order to get the table to display, I also wrote to a file called mars_table.html which was used in index.html to create the table. Mars_table.html will be updated when the website scrapes, should there be any changes to Mars attributes.

In the Mission_to_Mars folder, you will find my jupyter notebook which I did the inital exploration of each website. For 3 of the 4 websites, I used Splinter to access the pages and collect the information. As I indicated above, I used pandas to scrape the Mars facts to be display in a table which was converted to HTML.

Finally, my html files are stored in the templates folder and styles.css is stored in the static folder. This configuration was used inoder to design and style the final webpage. There are 2 screen shots of my final application stored in screenshots folder. This assignment was quite challenging and I had a lot of head scratching moments, but it was a lot of fun.
