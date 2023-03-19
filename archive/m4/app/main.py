from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import json


app = Flask(__name__)

data_df = pd.read_csv('database.tsv', sep='\t')
topic_dropdown = open('topic_dropdown.txt', 'r').readlines()

# Load index-link mappings
with open('index_to_link.json', encoding='utf-8') as f:
    index_to_link = json.load(f)


def search_readings(TOPIC, FORMAT, INCLUDE):
    TOPIC = '-'+TOPIC
    # Topic selection (Mandatory)
    selection = data_df[data_df.topics==TOPIC].copy()

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

    author_df = pd.DataFrame(author_df.author_individual.value_counts()).reset_index().rename(columns={'index': 'Author', 'author_individual': '# of Readings'})
    
    return (num_readings, num_courses), title_df, author_df, selection


@app.route('/', methods=("POST", "GET"))
def root():
    results = search_readings("Computer Science", 'All', 'All')
    reading_count = results[0][0]
    course_count = results[0][1]
    df = results[1]
    return render_template('index.html', topic_options=topic_dropdown, reading_count=reading_count, course_count=course_count, search_result_tables=[df.to_html(classes='data', header="true")])



@app.route('/results', methods=("POST", "GET"))
def search_results():
    results = search_readings(request.form['topic-selection'], request.form['format-selection'], request.form['include-selection'])
    reading_count = results[0][0]
    course_count = results[0][1]
    df = results[1]
    print(df)
    return render_template('index.html', topic_options=topic_dropdown, reading_count=reading_count, course_count=course_count, search_result_tables=[df.to_html(classes='data', header="true")])



if __name__ == '__main__':
    app.run(host='127.0.0.1')