# corpus_readme.md

## Package Requirement
- Python (>=3.7)
- selenium (>=4.0)
- webdriver-manager

## Getting Started
### Set Up
```
pip install selenium==4.0.0.a7
pip install webdriver-manager
```
#### Repo Structure
```
.
├── data
│   ├── raw     
│   └── concat
├── milestone_2
│   ├── indexer.py     
│   └── raw_text_scraper.py
```

#### Usage
```
python indexer.py
python raw_text_scraper.py
```
### Corpus

- source of the corpus: 
- collected corpus: https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/milestone2/milestone_2/data/concat (change it when merge)
- total number of documents: 2494
- total amount of text: ???

#### Storage
- link_to_index.json (create by indexer.py)
  - a json file which contains a dictionary. key is the link of the course, and value is the index id which we assign
  - link: https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/milestone2/milestone_2/data/index_to_link.json (change it when merge)
  - screenshot

- index_to_link.json (created by indexer.py)
  - a json file which contains a dictionary. key is the index id of the course, and value is link to the course
  - link: https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/milestone2/milestone_2/data/index_to_link.json (change it when merge)
  - screenshot

- concat/ (create by raw_text_scraper.py)
  - a folder of html files, and each of them contains concatenated sub-pages of the course. Each file is name by the course id (e.g. 0.html)
  - link: https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/milestone2/milestone_2/data/concat (change it when merge)
  - screenshot (folder)
  - screenshot (xx.html)

- raw/ (create by raw_text_scraper.py)
  - a folder of json files, and each is a dict of the source code of sub-pages. Key is the sub-page tile, and value is its source code.
  - link: https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/milestone2/milestone_2/data/raw (change it when merge)
  - screenshot (folder)
  - screenshot (xx.json)

### Problems With the Corpus
