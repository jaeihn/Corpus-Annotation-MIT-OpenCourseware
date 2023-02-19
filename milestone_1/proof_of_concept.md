- There are three files for scraping the course links, all sub-menu pages, and topics for each course. 

menu_scraper:
For each individual course, the code will first get all possible links in the homepage. Then it will filter out the irrelevant links and keep all the sub-menu links. The code will jump to each sub-menu link and scrape the raw text of that page. All the data is stored in a json file and is converted to a dataframe. 

topic_scraper:
For each course, the code will extract the topics covered by the course and save the information of the topics into a text file. The topics are multi-layered, with up to three layers. The code can grabs the information of the layers.