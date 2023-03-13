import requests
from bs4 import BeautifulSoup

from bs4.element import Comment
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
from urllib.request import urlopen

with open('index_to_link.json') as json_file:
    data = json.load(json_file)


def topic_info_extraction(link):
    txt = ""
    
    soup = BeautifulSoup(urlopen(link),"lxml")
    first_big_topic = ''
    round_value = 0

    #print(link)
    print()
    print('TOPICS\n')
    txt += 'TOPICS\n\n'

    for x in soup.find_all(["div"]):

        if "class" in x.attrs.keys() and x.attrs["class"] == ['position-relative', 'pt-1', 'pb-1', 'pl-4', 'ml-n2']:
            if x.get_text().replace("\n", "").strip() == first_big_topic:
                break
            print(x.get_text().replace("\n", "").strip())
            txt += x.get_text().replace("\n", "").strip() + '\n'
            if round_value == 0:
                first_big_topic = x.get_text().replace("\n", "").strip()
                round_value += 1

        if "class" in x.attrs.keys() and 'position-relative' in x.attrs["class"] and 'pt-1' in x.attrs["class"] and 'pb-1' in x.attrs["class"] and len(x.attrs["class"]) == 4:
            print("-" + x.get_text().replace("\n", "").strip())
            txt += "-" + x.get_text().replace("\n", "").strip() + '\n'

        if "id" in x.attrs.keys() and 'speciality-container' in x.attrs["id"] and x.get_text():
            print("--" + x.get_text().replace("\n", "").strip())
            txt += "--" + x.get_text().replace("\n", "").strip() + '\n'
    print()
    print()
    return txt

    
with open('0.txt', 'w') as f:
    f.write(topic_info_extraction(data['0']))
