import requests
from bs4 import BeautifulSoup
import regex
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
import time
import os 

from os import listdir
from os.path import isfile, join


print("START raw_text_scraper.py")


# Create directory, if it doesn't exist
path = "../"   # <---- You can change this path, if necessary

for p in ['data', 'data/raw', 'data/concat']:
    if not os.path.exists(path + p):
        os.makedirs(path + p)
        print(f"Directory {p} is created!\n")


data_path = "../data/"
raw_path = "../data/raw/"
concat_path = "../data/concat/"


# Load index-link mappings
f = open(data_path + 'index_to_link.json', encoding='utf-8') 
index_to_link = json.load(f)
f.close()
total_count = len(index_to_link)
print(f"Loaded {total_count} links.\n")



# Consider existing and missing files, continue downloading 
existing_files = {int(f.split('.')[0]) for f in listdir(raw_path) if isfile(join(raw_path, f)) and f.endswith('.json')}

missing_files = {i for i in range(total_count)}.difference(existing_files)
missing_files = list(missing_files)

print(f"Found {len(existing_files)} existing files, {len(missing_files)} missing files\n")


print("Start downloading sub-pages of each missing course . . .")


# Open headless browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

data = {}

# Download html content from each sub-page in each course page 
for file in tqdm(missing_files):
    i = str(file)
    link = index_to_link[i]

    data_per_course = {}

    soup = BeautifulSoup(requests.get(link).text, 'html.parser')

    # Get all routes
    all_routes = soup.find_all('a', href=True)
    matched_routes = set()
    for route in all_routes:
        if '/pages/' in route['href']:
            matched_routes.add('pages/' + route['href'].split('/pages/')[1])

    # Get all text from each route
    for sub_page in matched_routes:
        url = link + sub_page
        driver.get(url)

        if sub_page == 'syllabus':
            # Click expand description, if available
            try:
                driver.find_element(by=By.ID, value='expand-description').click()
            except NoSuchElementException:
                pass

        try: 
            # Extract text, if exists
            text = driver.find_element(by=By.ID, value='course-content-section').get_attribute('innerHTML')
            col_name = sub_page.split('/')[1].rstrip('/')

            data_per_course["html_concat"] = data_per_course.get("html_concat", "") + '\n\n' + col_name + '\n\n' + text 
            raw_text = regex.sub('\s', ' ', text)
            raw_text = ' '.join(raw_text.split())
            data_per_course[col_name] = raw_text
            data_per_course["link_to_page"] = link

        except NoSuchElementException:
            pass

    data[i] = {k: v for k, v in data_per_course.items() if k != 'html_concat'}
    
    # Save in folder
    with open(raw_path + i +'.json', 'w', encoding='utf-8') as f:
        json.dump(data_per_course, f, indent=4)
        f.close()

    with open(concat_path + i +'.html', 'w', encoding='utf-8') as f:
        f.write('<html> <meta charset="utf-8"/>' + data_per_course.get('html_concat','') + '</html>')
        f.close()

# Wait to finish
time.sleep(10)

# Load existing files, to join with the new files 
for file in listdir(raw_path):
    if isfile(join(raw_path, file)) and file.endswith('.json') and file not in data:
        index = file.split('.')[0]
        f = open(raw_path + index + '.json', encoding='utf-8') 
        data[index] = json.load(f)
        f.close()

# Final check, to see if we downloaded everything
if len(data) == total_count:
    with open(data_path + 'mit_ocw_courses.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("COMPLETE")
else: 
    print("DATA MISMATCH !!")
