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


def topic_info_extraction(data):
    
    # The dictionary to save all the topics
    my_dict = {}
    
    for index, link in data.items():
        
        # Checking progress
        if int(index) % 100 == 0:
            print(int(index))
    
        soup = BeautifulSoup(urlopen(link),"lxml")
        first_big_topic = ''
        round_value = 0

        topic_list = []

        for x in soup.find_all(["div"]):

            if "class" in x.attrs.keys() and x.attrs["class"] == ['position-relative', 'pt-1', 'pb-1', 'pl-4', 'ml-n2']:
                if x.get_text().replace("\n", "").strip() == first_big_topic:
                    break
                topic_list.append(x.get_text().replace("\n", "").strip())

                if round_value == 0:
                    first_big_topic = x.get_text().replace("\n", "").strip()
                    round_value += 1

            if "class" in x.attrs.keys() and 'position-relative' in x.attrs["class"] and 'pt-1' in x.attrs["class"] and 'pb-1' in x.attrs["class"] and len(x.attrs["class"]) == 4:
                topic_list.append("-" + x.get_text().replace("\n", "").strip())

            if "id" in x.attrs.keys() and 'speciality-container' in x.attrs["id"] and x.get_text():
                if x.get_text().replace("\n", "").strip() != '':
                    topic_list.append("--" + x.get_text().replace("\n", "").strip())

        my_dict[index] = topic_list
    
    print("Completed!")
    return my_dict

all_topics_dict = topic_info_extraction(data)

with open("all_topics.json", "w") as f:
    json.dump(all_topics_dict, f)
    f.close()