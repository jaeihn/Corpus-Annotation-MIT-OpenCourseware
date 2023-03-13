# Annotation + explanation + code

## Final number of annotations

### Fig. 1: Course Index Assignment

<img src="https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/screenshot/annotation_plan_batch.png" width="600" />

As discussed previously in [Milestone 2 Annotation Plan - Question 3](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/annotation_plan.pdf), we have distributed annotators at different course indices, with overlap. Because we had five people, Jessie was unmatched for Batch 1. Although we reported our expected number of unmatched courses as 1400 in the Annotation Plan (i.e. covering 700 courses, because two people annotate each course), we ended up with a total of 626 unmatched courses.

Mostly, we underestimated the time it takes to annotate one course, as well as the heavy workload of week 3, where we have other labs and quizzes. 

However, we realized that in terms of our project, our annotation "items" are not the courses, but rather each reading inside the course. Under such definitions, we have far greater number of annotations than we expected--a total of 17,987 raw annotations.

Below are some visualizations of annotated courses and readings by annotator. 

### Fig. 2: Number of Courses Annotated by Each Annotator
<img src="https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/screenshot/coursescount.png" width="600" />

### Fig. 3: Number of Readings Annotated by Each Annotator
<img src="https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/screenshot/annotationcount.png" width="600" />

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

These matching courses will be the basis of our [Interannotator Agreement Study](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/master/milestone_2/interannotator_agreement_study.ipynb).

-------

### Annotation Process 

Our latest [data](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/master/data) folder has the following structure. The links to these files (or the .zip, if they are too big) are listed below. 

```
├── data
│   ├── raw  
│   ├── concat 
│   ├── processed
│   └── parsed
```

- `raw` [[Milestone 2]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/corpus_collection.md) [[.zip file]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/data/raw.zip) [[raw_text_scraper.py]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/raw_text_scraper.py)
  - There are multiple sub-pages inside every course syllabus page listed in [MIT OpenCourseWare website](https://ocw.mit.edu/).
  - Content of each subpage was scraped using `selenium`, and saved in a `dict` object for that course. 
  - The contents of the `dict` was exported as a `.json` file, and put into the `raw` folder.
  - [Sample file in `raw`](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/data/raw/0.json)
- `concat` [[Milestone 2]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/corpus_collection.md) [[.zip file]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/data/concat.zip) [[raw_text_scraper.py]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_2/raw_text_scraper.py)
  - The html content from all of the subpages was combined (i.e. "concat"enated) into one long document. 
  - We added `<html />` and `<meta charset="utf-8"/>` tags in the beginning and end of document. 
  - We saved the concatenated file as `.html` in the `concat` folder.
  - [Sample file in `concat`](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/data/concat/0.html)
- `processed` [[directory]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/jae/data/processed) [[Python script]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/milestone_3/annotation_cleaner.py)
  - Our annotations are `str` containing the bibliography of the reading. 
  - This means there is many room for disagreement. A difference of even a single character--extra " ", missing "."--would make two annotations of the same reading look like different readings. 
  - We performed some `regex` filtering to reduce unintended differences as much possible. We included the following cases:
    - Strip new line characters
    - Strip asterisks (a lot of professors use * to differentiate between required/optional readings)
    - Strip `[Preview with Google Books]` links 
    - Strip various ways of `(PDF)` links - e.g. (PDF), (PDF - 12MB), (PDF 12MB), (PDF - 12.34MB), ....
    - Remove annotations shorter than 50 characters (these are likely to be table headings or comments on the readings--even if it is an annotation the information is too little for us to track down what the reading is referring to.) 
    - Remove duplicate annotations 
  - The script for filtering can be found [here](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/milestone_3/annotation_cleaner.py).
  - After applying the filter, the resulting .tsv files were put into the `processed` folder.
  - [Sample file in `processed`](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/data/processed/biya/1000.tsv)
- `parsed` [[directory]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/jae/data/parsed) [[Ruby script]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/milestone_3/annotation_parser.rb)
  - As an extension to our attempt in reducing unintended differences, we decided to extract specific information from the bibliography. 
  - For example, if two annotations refer to the same book, just different chapters, these two readings should be considered the same. If we are able to reduce the information to just the key parts, we should be able to match readings better. (our annotation decision was to only include the same book once)
  - This will also serve useful later on with our product, when we want to group the readings by author, journal, year, etc. 
  - We used a Ruby package called [AnyStyle](https://anystyle.io/). 
  - We wrote a script that automatically processes string bibliography in incoming .tsv files through AnyStyle. 
  - We chose the following hash keys from the AnyStyle parser:
    - Author
    - Title
    - Type (book, chapter, journal, etc.)
    - Collection (e.g. if journal article, what journal?)
    - Year 
  - New .tsv files with the old bibliographies replaced with parsed bibliographies were put in `parsed`. 
  - The Ruby script for parsing can be found [here](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/milestone_3/annotation_parser.rb). Please understand that we picked up Ruby soley to use this package, so the code may appear less proficient than the Python codes. 
  - [Sample file in '`parsed`](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/data/processed/biya/1000.tsv)

-------

### Final Version of Annotation

To produce the final version, we decided on the following rules on how to resolve conflicts in our interannotations:

- If both annotators agree on the category of the reading, we include it, as is. 
- If the annotators disagree on the category of the reading (one vote on "required, one vote on "optional"), we include the reading as "required". The rationale behind this is that it is better for a student to read the reading and find out that it was actually optional, than to not read the reading and find out later that it was actually required. 
- If one person annotated a reading that is completely missed by the other, we include the reading. In such cases, the person who _did_ annotate gets the say of the category.

You can find the related code in the [Python notebook here](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/master/milestone_3/final_annotations.ipynb)

This process generated two more folders in the `data` folder: 
- `dataframes` [[directory]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/jae/data/dataframes)
  - Any dataframes that were generated was exported to this directory, to be used by other code files. 
  - [Sample file in `dataframes`](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/data/dataframes/annotations_by_biya.tsv)
- `final` [[directory]](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/tree/jae/data/final)
  - Final version of annotations, only for the interannotated courses, were generated following the rules outlined in the next section.
  - We imitated the structure of our other annotation files, and saved them as .tsv.
  - [Sample file in `final`](https://github.ubc.ca/MDS-CL-2022-23/COLX523_BiyaIvanJaeJessieMin/blob/jae/data/final/0.tsv)

------

### How did the annotation process go? 

In the first week of our project, we assigned each of the five team members 250 curriculums/syllabi for annotation. Our discussions focused on identifying ambiguous elements and establishing guidelines, which we shared on Slack. We quickly realized that our expectation was too ambitious, so we greatly reduced the number of expected annotations for the following milestones. (This, too, turned out to be too high, considering the week 3 workload.)

As we started the interannotator analysis this week, we encountered inconsistencies in the quality of annotations. One of the members overlooked the fact that readings could also be in other sections, such as the course calendar. After finding this mistake, the annotator submitted revised version of annotations, which possible through the revised interface of our HTML Annotator. With this revision, our overall annotation quality was greatly improved.
