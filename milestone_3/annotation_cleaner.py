import os 

PATH_annotated = '../data/annotated='
for folder in os.listdir(PATH_annotated):
    for file in os.listdir(PATH_annotated + file):
        if file.endswith('.tsv'):
            with open(PATH_annotated + file) as f:
                annotations = f.readlines()

                print(annotations)
                break