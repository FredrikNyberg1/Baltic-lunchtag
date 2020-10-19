import csv
import pandas

with open('tags_20201012.csv') as file:
    spamreader = csv.reader(file, delimiter=' ', quotechar='|')
    reader = csv.reader(file)
    for row in reader:
        pandas