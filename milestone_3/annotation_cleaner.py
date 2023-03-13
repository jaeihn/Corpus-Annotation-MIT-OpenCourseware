import os 
import re
from unidecode import unidecode

PATH_annotation = '../data/annotated/'
PATH_processed = '../data/processed/'
PATH_parsed = '../data/parsed/'

# Preparing directories 
for folder in [PATH_processed]+[PATH_processed+dir+'/' for dir in os.listdir(PATH_annotation) if dir != '.DS_Store']:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Directory created at {folder}!")

for folder in [PATH_parsed]+[PATH_parsed+dir+'/' for dir in os.listdir(PATH_annotation) if dir != '.DS_Store']:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Directory created at {folder}!")

# Filtering step 
for folder in os.listdir(PATH_annotation):
    if os.path.isdir(PATH_annotation + folder):
        for file in os.listdir(PATH_annotation + folder):
            if file.endswith('.tsv'):
                with open(PATH_annotation + folder + '/' + file, 'r', encoding='utf-8') as f_in, open(PATH_processed + folder + '/' + file, 'w', encoding='utf-8') as f_out:
                    prev_reading = ""
                    unique_annotations = set()
                    for line in f_in:
                        if line == "":
                            continue
                        category, annotation = line.split('\t',1)

                        # Strip new line 
                        annotation = annotation.rstrip('\n')
                        # Strip astericks
                        annotation = re.sub(r"\*", "", annotation)

                        # Strip Links to Google Books 
                        annotation = re.sub(r"\[Preview (in|with) Google Books\]", "", annotation)
                        # Strip PDF 
                        annotation = re.sub(r"\( ?PDF ?(-)? ?\d*(\.)?\d* ?M?B?\)", "", annotation)
                        # Strip "forthcoming"
                        annotation = re.sub(r"\(forthcoming\)", "", annotation)
                        # Strip whitespace
                        annotation = annotation.strip(' ')
                        # Strip period
                        annotation = annotation.rstrip('.')
                        if len(annotation) <50:
                            continue
                        if annotation not in unique_annotations:
                            unique_annotations.add(annotation)
                            f_out.write(category + "\t" + annotation + "\n")

print("Complete!!!")
