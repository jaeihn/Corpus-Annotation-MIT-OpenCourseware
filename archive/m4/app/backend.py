import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import nltk
nltk.download("brown")
nltk.download("universal_tagset")
from nltk.corpus import brown
from collections import defaultdict
import numpy as np
from random import random


app = FastAPI()


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

@app.get("/pos")
def display_pos_table(output, genre):
    print("here!")
    if output == "table":
        return HTMLResponse(put_in_table(get_POS_distribution(genre)))
    elif output == "graph":
        save_bar_graph(get_POS_distribution(genre), "pos.png")
        return HTMLResponse(f'<img src="pos.png?t={random()}" />')

@app.get("/{filename}")
def pass_file(filename):
    return FileResponse(filename)

@app.get("/")
def start():
    return FileResponse("front_end.html")


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999, debug=True)



