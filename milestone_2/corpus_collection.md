# Corpus Collection Code Explanation

## Introduction 

- The corpus collection code files can be found in the `milestone_2` directory. We provide the links below:
  - `indexer.py` - link to index
  - `raw_text_scraper.py` - link to raw index
- There are comments throughout both of the code files, for each step. 
- The purpose of this document is to extend those comments and provide more information about the code and our decisions around corpus collection. 

---------

## Frozen Corpus 

- The MIT OCW website updates periodically. This means that the course search results and the indexing of those courses are different from `milestone_1`. 
- To prevent future updates in affecting our entire pipeline and corresponding reports, we have downloaded our full corpus on February 26, 2023, and "froze" those files.
- You can find our corpus in the `data` directory. Below are the links: 
  - mit ..
  - .
  - .
- You are welcome to run the corpus collection code to check how the corpus is collected, but please note that the export file may be different from our frozen corpus.

--------

## Preparation 

### Libraries

The two files have dependencies on the following libraries, which you may not have: 
```bash
pip install selenium==4.0.0.a7
pip install webdriver-manager
pip install progressbar
pip install tqdm
```

The two files also import from other libraries, which you probably already have: 
```python
time
json
requests
regex
bs4        # BeautifulSoup
os
```

### Directory Setup / Paths

```
├── data
│   ├── raw     
│   └── concat
├── milestone_2
│   ├── corpus_collection.md      # CURRENT DOCUMENT  
│   ├── indexer.py     
│   └── raw_text_scraper.py
```

- Output files are exported to the `data` directory, which should be in the parent directory of the one that contains the code.
  - In our case, the code is in `milestone_2`, and the parent directory is the `root` directory.
- At the beginning, the code file checks if the necessary directories exist. If not, it will create those directories. 
- You can edit the paths at the beginning of the code file, if you wish to use another path. 

------

## In-Depth Explanation for `indexer.py` 

This script: 
- Takes no input.
- Takes about 3~5 minutes to run. 
  - Because the runtime is short, we did not implement start-restart ability. (`raw_text_scraper.py` does!)
- Outputs two files into the `data` folder:
  - `link_to_index.json` - Contains mappings from course page URL links to indices.
  - `index_to_link.json` - Contains mappings from indices to course page URL links. 
- Using a `selenium` browser, the script will perform the following tasks:
  - Connect to our corpus source: https://ocw.mit.edu/courses/
  - Switch the layout of search results from "pretty" to "compact". 
    - The "pretty" layout is spacious, include images for each course, shows professor and topics, etc. 
    - The "compact" layout is much narrower than the "pretty" layout, which means we are able to fit more courses in the same amount of height. This results in less scrolling and less time. 
    - The `while`-loop waits until the buttons are loaded, then `selenium` clicks on the button. 
  - Find the total number of results.
    - This information is used to determine whether we have found all available course results. 
    - The `while`-loop waits until the total number is printed on the page, then `selenium` retrieves this value. 
  - Scroll to the very VERY bottom of the page.
    - The MIT OCW homepage shows course search results in a fluid container. This means that it does not have "pages" to organize the search results, as in Google. More search results are shown only when users scroll to the bottom of the page. 
    - This means that, to retrieve all search results, we must keep scrolling until we reach the very VERY bottom. This is when the total number of results above becomes useful. 
    - The `while`-loop is used for continuous scrolling, and only breaks when we have reached the total number of search results. 
  - Extract URL links to course pages. 
    - Once the scrolling is complete, we have all courses (aronud 2500) in one page. 
    - `selenium` retrieves `a href` links that follow pattern: "https://ocw.mit.edu/courses/ ... course name ... "
       - Example course page: https://ocw.mit.edu/courses/1-00-introduction-to-computers-and-engineering-problem-solving-spring-2012/pages/syllabus/
 - Creates two index mappings.
    - This code section does not involve `selenium`. 
    - It takes the links found by `selenium` above, and enumerates the unique links with indices. Duplicate links are removed. 
    - One dictionary maps the links to indices, another dictionary maps the indices to links. 
 - Exports index mappings as file. (See above.) 


-------

## In-Depth Explanation for `indexer.py` 

This script: 
- Takes no input.
- Takes about 3~5 minutes to run. 
  - Because the runtime is short, we did not implement start-restart ability. (`raw_text_scraper.py` does!)
- Outputs two files into the `data` folder:
  - `link_to_index.json` - Contains mappings from course page URL links to indices.
  - `index_to_link.json` - Contains mappings from indices to course page URL links. 
- Using a `selenium` browser, the script will perform the following tasks:
  - Connect to our corpus source: https://ocw.mit.edu/courses/
  - Switch the layout of search results from "pretty" to "compact". 
    - The "pretty" layout is spacious, include images for each course, shows professor and topics, etc. 
    - The "compact" layout is much narrower than the "pretty" layout, which means we are able to fit more courses in the same amount of height. This results in less scrolling and less time. 
    - The `while`-loop waits until the buttons are loaded, then `selenium` clicks on the button. 
  - Find the total number of results.
    - This information is used to determine whether we have found all available course results. 
    - The `while`-loop waits until the total number is printed on the page, then `selenium` retrieves this value. 
  - Scroll to the very VERY bottom of the page.
    - The MIT OCW homepage shows course search results in a fluid container. This means that it does not have "pages" to organize the search results, as in Google. More search results are shown only when users scroll to the bottom of the page. 
    - This means that, to retrieve all search results, we must keep scrolling until we reach the very VERY bottom. This is when the total number of results above becomes useful. 
    - The `while`-loop is used for continuous scrolling, and only breaks when we have reached the total number of search results. 
  - Extract URL links to course pages. 
    - Once the scrolling is complete, we have all courses (aronud 2500) in one page. 
    - `selenium` retrieves `a href` links that follow pattern: "https://ocw.mit.edu/courses/ ... course name ... "
       - Example course page: https://ocw.mit.edu/courses/1-00-introduction-to-computers-and-engineering-problem-solving-spring-2012/pages/syllabus/
 - Creates two index mappings.
    - This code section does not involve `selenium`. 
    - It takes the links found by `selenium` above, and enumerates the unique links with indices. Duplicate links are removed. 
    - One dictionary maps the links to indices, another dictionary maps the indices to links. 
 - Exports index mappings as file. (See above.) 


----- 


We have decided not to apply any filters on the initial collection. Previously, we were going to filter on the "sub-pages" of each website. For example, 
But it could be added here if necessary. 
Therefore, we decided to include all without filtering for our task. 

If filtering is needed, it can be done here. 

