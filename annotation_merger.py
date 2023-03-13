import os
import argparse
import glob 


END = "====================== END ======================\n"

parser = argparse.ArgumentParser("Annotation generator")
parser.add_argument('annotator', metavar='annotator', type=str, nargs=1, help='name of annotator or annotator directory in data/annotated/')
# parser.add_argument('course_number', metavar='course_number', type=str, nargs=1, help='.html file')
# parser.add_argument('annotator', type=str, nargs=1, help='name of annotator (or annotator folder name)')
parser.add_argument('-i', "--interactive", action='store_true', help='run interactively')
parser.add_argument('-o', "--overwrite_all",  action='store_true', help='overwrite all .tsv')
parser.add_argument('-s', "--skip_existing",  action='store_true', help='skip all existing .tsv')

args = parser.parse_args()
args = vars(args)

annotator = args['annotator'][0]
PATH_TSV = '../data/annotated/' + annotator + '/tsv/'
PATH_TXT = '../data/annotated/' + annotator + '/txt/'
overwrite = args['overwrite_all']
interactive = args['interactive']
skip = args['skip_existing']

if overwrite + interactive + skip== 0:
    print("Must choose one of -i / -o / -s mode.")
    exit()
# course_number = args['course_number'][0]
# annotator = args['annotator'][0]
print()

path = '../'
for p in ['data', 'data/annotated', 'data/annotated/'+ annotator, 'data/annotated/'+ annotator + '/tsv', 'data/annotated/'+ annotator + '/txt']:
    if not os.path.exists(path + p):
        os.makedirs(path + p)
        print(f"Directory {p} is created!")
print()


def merge(course_number):

    count_r, count_o, count_total = 0, 0, 0

    print(f"====================== {course_number} ======================\n")

    # Check for overwrite 
    if overwrite:
        with open(PATH_TSV + course_number + '.tsv', 'w') as f_final:
            pass
    elif interactive:
        if os.path.exists(PATH_TSV + course_number + '.tsv'):
            print(f"A .tsv file for {course_number} already exists.\n")
            while True:
                response = input("Are you sure you you want to overwrite? (y/n)")
                if response in ['y', 'Y']:
                    with open(PATH_TSV + course_number + '.tsv', 'w') as f_final:
                        break
                if response in ['n', 'N']:
                    print("Skipping to next ... ")
                    break


    # Append required readings
    if os.path.exists(PATH_TXT + course_number + '_r' + '.txt'):
        print("Found -r .txt file")
        with open(PATH_TXT + course_number + '_r' + '.txt', 'r') as f_req,  open(PATH_TSV + course_number + '.tsv', 'a+') as f_final:
            for line in f_req:
                if line == '' or line == '\n':
                    continue
                line = line.strip()
                line = line.strip("")
                count_r += 1
                count_total += 1 
                f_final.write('Required\t' + line + '\n')
    else:
        print("Could not find -r .txt file")


    # Append optional readings
    if os.path.exists(PATH_TXT + course_number + '_o' + '.txt'):
        print("Found -o .txt file")
        with open(PATH_TXT + course_number + '_o' + '.txt', 'r') as f_opt,  open(PATH_TSV + course_number + '.tsv', 'a+') as f_final:
            for line in f_opt:
                if line == '' or line == '\n':
                    continue
                line = line.strip()
                line = line.strip("")
                count_o += 1
                count_total += 1
                f_final.write('Optional\t' + line + '\n')
    else:
        print("Could not find -o .txt file")

    # Is it empty? 
    if count_r + count_o == 0:
        with open(PATH_TSV + course_number + '.tsv', 'w') as f_final:
            pass
        # response = input("No readings were found. Create empty .tsv? (y/n) ")
        # while True:
        #     if response in ['y', 'Y']:
        #         with open(PATH + course_number + '.tsv', 'w') as f_final:
        #             break
        #     elif response in ['n', 'N']:
        #         print("Aborting ... \n")
        #         print(END)


    check_lines = 0

    with open(PATH_TSV + course_number + '.tsv', 'r') as f_final:
        for line in f_final:
            check_lines += 1

    if check_lines == count_total and check_lines == (count_o + count_r):
        print()
        print(f"Number of REQUIRED readings: {count_r}")
        print(f"Number of OPTIONAL readings: {count_o}")
        print(f"Number of TOTAL readings: {count_total}\n")

        print(f"{course_number}.tsv file generated.")
#        print(END)
#        exit()
    else:
        print("Mismatch in number of readings. Check your files, then try again.\n")

#        exit()
    return 



        

tsv_files = set()
txt_files = set()

for f in os.listdir(PATH_TSV):
    filename = f.split(".")[0]
    exten = f.split(".")[-1]
               
    if exten == 'tsv':
        tsv_files.add(filename)


for f in os.listdir(PATH_TXT):
    filename = f.split(".")[0]
    exten = f.split(".")[-1]
               
    if exten == 'txt': 
        if filename.split("_")[0] == filename:
            pass
        else:
            txt_files.add(filename.split("_")[0])

if skip:
    queue = txt_files.difference(tsv_files)
elif overwrite or interactive:
    queue = txt_files

queue = sorted(list(queue), key=lambda x: int(x))

print("Files to create　▼ ")

for q in queue:
    print(q)


for q in queue:
    merge(q)


print(END)