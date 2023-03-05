# imports
import time
import requests
import selenium
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Gather all course urls 
url = 'https://ocw.mit.edu/courses/'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)


# switch to condensed layout
driver.find_element(by=By.CLASS_NAME, value='layout-button-right').click()


# Scroll to bottom of page
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# Scrape links
links = driver.find_elements(by=By.XPATH, value="//a[.//span[starts-with(@id, 'search-result-')]]")
links = [l.get_attribute('href') for l in links]


# Create index mapping
link_to_index = {}
index_to_link = {}

for i, link in enumerate(links):
	link_to_index[link] = i
	index_to_link[i] = link


# Export files 
with open("../data/link_to_index.json", "w") as f:
    json.dump(link_to_index, f)
    f.close()

with open("../data/index_to_link.json", "w") as f:
    json.dump(index_to_link, f)
    f.close()    
