import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# Function to scrape for weather in Cost Rica
def scrape():

    # Initialize browser
    browser = init_browser()

    # Visit the Costa Rica climate site
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    # Scrape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all(class_='itemLink product-item')


    # Store in dictionary
    hemisphere_image_urls =[]
    # Loop through returned results
    for result in results:
        # Error handling
        try:
            title = result.find('h3').text
            link = "http://astropedia.astrogeology.usgs.gov/download/"+ result['href'][12:]+'.tif/full.jpg'
            if (title and link):
                # Print results
                print('-------------')
                print(title)
                print(link)

                # Dictionary to be inserted as a MongoDB document
                post = {
                    "title": title,
                    "img_url": link
                }
                hemisphere_image_urls.append(post)
                

                #collection.insert_one(post)

        except Exception as e:
            print(e)
            
    print('this is the hemisphere:', hemisphere_image_urls)

    # Return results
    return hemisphere_image_urls

    
