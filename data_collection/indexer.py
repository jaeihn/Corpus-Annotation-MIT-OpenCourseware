# imports
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

PAUSE_TIME = 3

print("STARTING indexer.py")

# Gather all course urls 
url = 'https://ocw.mit.edu/courses/'

# Open up headless browser 
# https://stackoverflow.com/questions/7593611/selenium-testing-without-browser
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
driver.get(url)

# Switch layout by clicking button, for less scrolling
while True:
    try: 
        layout_button = driver.find_element(by=By.CLASS_NAME, value='layout-button-right')
        layout_button.click()
        print("Loaded layout button.\n")
        break
    except NoSuchElementException:
        print("Waiting for layout button to load . . .")
    time.sleep(PAUSE_TIME)

# Find total results count element
while True: 
    try: 
        total_count = driver.find_element(by=By.XPATH, value='//span[@class="results-total-number"]')
        total_count = int(total_count.text)
        print("Loaded results total count.\n")
        break
    except NoSuchElementException:
        print("Waiting for results total count to load . . .")
    time.sleep(PAUSE_TIME)


# Scroll to bottom of page, until last element (== total results number) is found 
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python

print("Finding search results . . . ")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Stop when 
    try:
        last_article = driver.find_element(by=By.XPATH, value="//article[@aria-posinset="+str(total_count)+"]")
        break
    except:
        pass

# Find elements corresponding to course syllabus pages 
search_results = driver.find_elements(by=By.XPATH, value="//article/descendant::a[@href]")
print(f"{len(search_results)} active links results found.\n")

print("Creating index mappings . . .")
# Extract links 
links = [l.get_attribute('href') for l in search_results]

# Create index mapping
link_to_index = {}
index_to_link = {}

duplicate_count = 0

for i, link in enumerate(links):
    if link in link_to_index:
        duplicate_count += 1    
    link_to_index[link] = i
    index_to_link[i] = link

# Export files 
with open("../data/link_to_index.json", "w") as f:
    json.dump(link_to_index, f)
    f.close()

with open("../data/index_to_link.json", "w") as f:
    json.dump(index_to_link, f)
    f.close()    

print(f"Found {duplicate_count} duplicate links.\n")
print(f"Course-index mappings of {len(link_to_index)} courses EXPORT COMPLETE !!")