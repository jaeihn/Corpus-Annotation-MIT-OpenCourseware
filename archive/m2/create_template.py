import json
import os

index_to_link_path = '../data/index_to_link.json'
annotation_path = '../data/annotation/'


def create_folder(dir_path):
    if not os.path.exists(dir_path):
        # Create a new directory because it does not exist
        os.makedirs(dir_path)
        print(f"The new directory {annotation_path} is created!")


def create_all_templates():
    create_folder(annotation_path)

    f = open(index_to_link_path, encoding='utf-8')
    index_to_link = json.load(f)
    f.close()

    for i in index_to_link:
        with open(annotation_path + i + '.txt', 'w') as f:
            f.write("# REQUIRED\n\n")
            f.write("# OPTIONAL\n\n")


if __name__ == "__main__":
    create_all_templates()