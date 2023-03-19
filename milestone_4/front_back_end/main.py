import numpy as np
import pandas as pd
import json
from fastapi import Response

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from nltk.corpus import brown
from collections import defaultdict
from random import random
from urllib import parse

from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")


templates = Jinja2Templates(directory="templates")


data_df = pd.read_csv('database.tsv', sep='\t')
topic_dropdown = open('topic_dropdown.txt', 'r').readlines()

# Load index-link mappings
with open('index_to_link.json', encoding='utf-8') as f:
    index_to_link = json.load(f)


def search_readings(TOPIC, FORMAT, INCLUDE):
    TOPIC = '-' + TOPIC
    # Topic selection (Mandatory)
    selection = data_df[data_df.topics == TOPIC].copy()

    # Format selection (if specified)
    if FORMAT in ['Book', 'Paper']:
        selection = selection[selection.type == FORMAT]

    # Include categories (if specified)
    if INCLUDE == 'Required':
        selection = selection[selection.category == 'Required']
    elif INCLUDE == 'Optional':
        selection = selection[selection.category == 'Optional']

    num_courses = len(selection.course.unique())
    num_readings = selection.shape[0]

    title_df = selection.copy()
    title_df = title_df.sort_values('title')
    title_df['Link to Course'] = title_df.course.apply(lambda x: index_to_link[str(x)])
    title_df = title_df.drop(columns=['type', 'author_individual', 'course', 'topics'])
    title_df = pd.DataFrame(title_df.value_counts()).reset_index()
    title_df = title_df.drop(columns=['category', 0])

    author_df = selection.copy()
    author_df = author_df.drop(columns=['author', 'topics'])
    author_df = author_df.explode('author_individual')

    author_df = pd.DataFrame(author_df.author_individual.value_counts()).reset_index().rename(
        columns={'index': 'Author', 'author_individual': '# of Readings'})

    return (num_readings, num_courses), title_df, author_df, selection


def save_bar_graph(pos_dict,filename):
    sorted_pos = sorted(pos_dict.keys(),key=lambda x: pos_dict[x],reverse=True)
    nums = [pos_dict[pos] for pos in sorted_pos]
    ticks = np.arange(0,len(nums))

    plt.bar(ticks, nums, width=0.5, align='center')
    plt.xticks(ticks,sorted_pos,rotation=60)

    plt.savefig(filename)
    plt.clf()


def get_POS_distribution(category):
    pos_counts = defaultdict(int)
    for word,pos in brown.tagged_words(categories=category,tagset="universal"):
        pos_counts[pos] += 1
    return pos_counts


def create_row(items):
    S = []
    S.append("<tr>")
    for item in items:
        S.append('<td class="cell">' + str(item) + "</td>")
    S.append("</tr>")
    return "".join(S)


def put_in_table(dictionary):
    return "<table>" + create_row(dictionary.keys()) + create_row(dictionary.values()) + "</table>"

@app.get("/search-by-title")
def search_by_title(topicselection, formatselection, includeselection):
    results = search_readings(topicselection[:-1], formatselection, includeselection)
    reading_count = results[0][0]
    course_count = results[0][1]
    df = results[1]
    # return HTMLResponse(topicselection)
    message = "<p>Found " + str(reading_count) + " readings for " + str(course_count) + " courses</p>"
    if reading_count == 0:
        return HTMLResponse(message)
    else:
        return HTMLResponse(message + df.to_html(classes='data', header='true'))

@app.get("/search-by-author")
def search_by_author(topicselection, formatselection, includeselection):
    results = search_readings(topicselection[:-1], formatselection, includeselection)
    df = results[2]
    return HTMLResponse(df.to_html(classes='data', header='true'))

@app.get("/")
def start():
    return FileResponse("index.html")

@app.get("/index.html")
def start():
    return FileResponse("index.html")

@app.get("/statistics.html")
def start():
    return FileResponse("statistics.html")

# @app.get("/search-by-title.html")
# async def read_search(topics: str = 'Computer Science', formats: str = 'All', include : str = 'All'):
#     print(topics)
#     return FileResponse("search-by-title.html")

# @app.get("/search-by-title.html")
# async def read_item(topics: str = 'Computer Science', formats: str = 'All', include : str = 'All'):
#     results = search_readings(topics, formats, include)
#     return results[1]

@app.get("/search-by-title.html")
def start(request: Request):
    return templates.TemplateResponse(
        'search-by-title.html',
        context={
            'request': request,
            'topic_options': topic_dropdown, 
            })

@app.get("/search-by-author.html")
def start(request: Request):
    return templates.TemplateResponse(
        'search-by-author.html',
        context={
            'request': request,
            'topic_options': topic_dropdown, 
            })

# @app.get("/search-by-title/")
# async def start(request: Request, topics: str = 'Computer Science', formats: str = 'All', include: str = 'All'):
#     results = search_readings(topics, formats, include)
#     reading_count = results[0][0]
#     course_count = results[0][1]
#     title_df = results[1]
#     return templates.TemplateResponse(
#         'search-by-title.html', 
#         context={
#             'request': request,
#             'topic_options': topic_dropdown, 
#             'reading_count': reading_count,
#             'course_count': course_count,
#             'search_result_tables': [title_df.to_html(classes='data', header="true")]
#             })



# @app.get("/questions")
# def load_questions():
#     return Response(data_df.to_json(orient="records"), media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999, debug=True)

#     @app.route('/results', methods=("POST", "GET"))
# def search_results():
#     results = search_readings(request.form['topic-selection'], request.form['format-selection'], request.form['include-selection'])
#     reading_count = results[0][0]
#     course_count = results[0][1]
#     df = results[1]
#     print(df)
#     return render_template('index.html', topic_options=topic_dropdown, reading_count=reading_count, course_count=course_count, search_result_tables=[df.to_html(classes='data', header="true")])

