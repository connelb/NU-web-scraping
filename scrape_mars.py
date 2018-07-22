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


    # Store in dictionary
    weather = {}

    # Return results
    return weather