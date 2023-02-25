from bs4 import BeautifulSoup
import json
from os import listdir
from os.path import isfile, join
from create_template import *

html_path = "../data/examples"  # change the path to the folder which contains html files (eg. "../data/concat")
all_books = "../data/possi_books/"  # output folder
index_to_link = '../data/index_to_link.json'


onlyfiles = [f for f in listdir(html_path) if f.endswith('.html')]
print(onlyfiles)


def grab_possible_book():
    # if the folder possi_books does not exist, create it
    create_folder(all_books)

    for file in listdir(html_path):
        if isfile(join(html_path, file)) and file.endswith('.html'):
            with open(join(html_path, file)) as fp:
                soup = BeautifulSoup(fp, 'html.parser')
                i = file.split('.')[0]

                # Get all italics
                all_italics = soup.findChildren('em')

                with open(all_books + i + '.txt', 'w') as f:
                    for item in all_italics:
                        f.write(item.parent.text+"\n\n")


if __name__ == "__main__":
    grab_possible_book()