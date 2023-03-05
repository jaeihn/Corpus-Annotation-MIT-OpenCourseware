import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import regex
import selenium
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
# Opening JSON file
f = open('../data/index_to_link.json')
 
# returns JSON object as 
# a dictionary
index_to_link = json.load(f)

print(index_to_link)
 
f.close()

links = [index_to_link['0']]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for link in links:

    data_per_course = {}

    soup = BeautifulSoup(requests.get(link).text, 'html.parser')

    # Get all routes
    all_routes = soup.find_all('a', href=True)
    matched_routes = []
    for route in all_routes:
        if '/pages/' in route['href']:
            matched_routes.append('pages/' + route['href'].split('/pages/')[1])
    matched_routes.remove('pages/privacy-and-terms-of-use/')

    # Get all text from each route
    for sub_page in matched_routes:

        if sub_page == 'syllabus':
            # Click expand description
            driver.find_element(by=By.ID, value='expand-description').click()

        url = link + sub_page

        driver.get(url)
        text = driver.find_element(by=By.ID, value='course-content-section').text
        text = regex.sub('\s', ' ', text)
        col_name = sub_page.split('/')[1].rstrip('/')
        raw_text = ' '.join(text.split())

        data_per_course[col_name] = raw_text


    with open('../data/raw/0.json', 'w') as f:
        json.dump(data_per_course, f)
    
