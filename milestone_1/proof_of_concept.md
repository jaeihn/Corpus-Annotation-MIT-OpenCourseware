# COLX 523 Proof of Concept

There are three files for the scraping, corresponding to different parts of our scraping. 
Because `indexer.py` involves "scrolling down" 2505 search results, we provide its output in `data` folder. 
(It takes about 2-3 minutes, if you'd like to run it.)

## `indexer.py` 

- This file uses a library called `selenium` to scrape all course links from `https://ocw.mit.edu/courses/`.
- The coruse catalog in the website is not divided into pages with fixed number of results on each page (like in Google search results).
- Instead, the contents are in a container with variable height that updates when the user scrolls down.
- After the browser is loaded, there is a while-loop that automatically scrolls down to the bottom of the page.
- When the website does not increase anymore, we have reached all coruses. 
- The file looks for relevant links with the correct path, that correpsonds to each course. 
- The file creates mappings for index-to-links and links-to-index, and exports the dictionaries as a json file.

## `raw_text_scraper.py`

- The file loads the index-to-link dictionary outputted by the `indexer.py` file. 
- For each individual course link, the code will first get all possible sub-page links in the homepage. 
- Then it will filter out the irrelevant links and keep all the sub-menu links. 
- The code will jump to each sub-menu link and scrape the raw text of that page. 
- All the data is stored in a json file and is converted to a dataframe. 


## `topic_scraper.py`

- For each course, the code will extract the topics covered by the course and save the information of the topics into a text file. 
- The information is extracted from the main page of the course syllabus page. 
- The topics are multi-layered, with up to three layers. The code can grabs the information of the layers.
