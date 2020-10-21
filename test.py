import csv
import pandas as pd

taggar_csv = pd.read_csv('taggar.csv')

i = 0

klasser = taggar_csv.columns

tags = []

klass_lunch = []

for klass in klasser:
    klass_tags = taggar_csv[klasser[i]].to_list()
    tags.extend(klass_tags)
    i += 1

for tag in tags:
    tag = int(input("Input tag: "))
    if tag in tags:
        print("Du får äta här!")
    else:
        print("Du får inte äta här...")