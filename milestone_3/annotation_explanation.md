# Annotation + explanation + code

## Final number of annotations

### Fig. 1: Course Index Assignment

<img src="https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/screenshot/annotation_plan_batch.png" width="600" />

As discussed previously in [Milestone 2 Annotation Plan - Question 3](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/annotation_plan.pdf), we have distributed annotators at different course indices, with overlap. Because we had five people, Jessie was unmatched for Batch 1. Although we reported our expected number of unmatched courses as 1400 in the Annotation Plan (i.e. covering 700 courses, because two people annotate each course), we ended up with a total of 626 unmatched courses.

Mostly, we underestimated the time it takes to annotate one course, as well as the heavy workload of week 3, where we have other labs and quizzes. 

However, we realized that in terms of our project, our annotation "items" are not the courses, but rather each reading inside the course. Under such definitions, we have far greater number of of annotations than we expected--a total of 17,987 raw annotations.

Below are some visualizations of annotated courses and readings by annotator. 

### Fig. 2: Number of Courses Annotated by Each Annotator
<img src="https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/screenshot/courses_stats.png" width="600" />

### Fig. 3: Number of Readings Annotated by Each Annotator
<img src="https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/screenshot/annotation_stats.png" width="600" />

The numbers reported in `Fig. 2` are unmatched courses. Below is a table of actual course indices covered by each annotator: 

| Annotator | Course Index | Count |
|:---------:|:-------:|:-----:|
| Min | 0 - 180 | 180 | 
| Ivan | 0 - 131 | 131 | 
| Bingyang | 1000 - 1090<br>1096-1110 | 105 | 
| Jae | 1000 - 1093<br>1242 - 1250 | 102 | 
| Jiexin | 1532 - 1640 | 108 | 

Therefore, there were two annotator pairs in our project:

| Pair | Matching Course Index | Count |
|:----:|:---------------------:|:-----:|
| Biya-Jae | 1000 - 1090 | 90 | 
| Min-Jinhong | 0 - 131 | 131 | 

These matching courses will be the basis of our [Interannotor Agreement Study].

### Annotation Process 

Our latest [data](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/master/data) folder has the following structure. We provide one sample file inside each of the folder, and include the full contents of the folder as a .zip file, because the full files are too big to include on Github.

```
├── data
│   ├── raw  
│   ├── concat 
│   ├── processed
│   └── parsed
```

- `raw` [[Milestone 2]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/corpus_collection.md) [[raw_text_scraper.py]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/raw_text_scraper.py)
  - There are multiple sub-pages inside every course syllabus page listed in [MIT OpenCourseWare website](https://ocw.mit.edu/).
  - Content of each subpage was scraped using `selenium`, and saved in a `dict` object for that course. 
  - The contents of the `dict` was exported as a `.json` file, and put into the `raw` folder.
- `concat` ([Milestone 2](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/corpus_collection.md)) [[raw_text_scraper.py]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/raw_text_scraper.py)
  - The html content from all of the subpages was combined (i.e. "concat"enated) into one long document. 
  - We added `<html />` and `<meta charset="utf-8"/>` tags in the beginning and end of document. 
  - We saved the concatenated file as `.html` in the `concat` folder.
- `processed` []()
  - Our annotations are `str` containing the bibilography of the reading. 
  - This means there is many room for disagreement. A difference of even a single character--extra " ", missing "."--would make two annotations of the same reading look like different readings. 
  - We performed some `regex` filtering to reduce unintended differences as much possible. We included the following cases:
    - Strip new line characters
    - Strip astericks (a lot of professors use * to differentiate between required/optional readings)
    - Strip `[Preview with Google Books]` links 
    - Strip various ways of `(PDF)` links - e.g. (PDF), (PDF - 12MB), (PDF 12MB), (PDF - 12.34MB), ....
    - Remove annotations shorter than 50 characters (these are likely to be table headings or comments on the readings--even if it is an annotation the information is too little for us to track down what the reading is referring to.) 
    - Remove duplicate annotations 
  - The script for filtering can be found []().
  - After applying the filter, the resulting .tsv files were put into 
- `parsed` []()
  - As an extention to our attempt in reducing unintended differences, we decided to extract specific information from the bibligraphy. 
  - For example, if two annotations refer to the same book, just different chapters, these two readings should be considered the same. If we are able to reduce the information to just the key parts, we should be able to match readings better. (our annotation decision was to only include the same book once)
  - This will also serve useful later on with our product, when we want to group the readings by author, journal, year, etc. 
  - We used a Ruby package called [AnyStyle](https://anystyle.io/). 
  - We wrote a script that automatically processes string bibliography in incoming .tsv files through AnyStyle. 
  - We chose the following hash keys from the AnyStyle parser:
    - Author
    - Title
    - Type (book, chapter, journal, etc.)
    - Collection (e.g. if journal artical, what journal?)
    - Year 
  - New .tsv files with the old bibliographies replaced with parsed bibliographies were put in `parsed`. 
  - The Ruby script for parsing can be found here. Please understand that we picked up Ruby soley to use this package, so the code may not be ideal.

### Final Version of Annotation



### How did the annotation process go? 
