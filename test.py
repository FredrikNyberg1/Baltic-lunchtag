import csv
import pandas as pd
import time

df = pd.read_csv('taggar.csv')

tag = int(input("Input tag: "))

i = 0

klasser = df.columns

tags = []


for klass in klasser:
    # print(klasser[i])
    klass_tags = df[klasser[i]].to_list()
    # print(klass_tags)
    tags.extend(klass_tags)
    # print(tags)
    i += 1

if (tag in tags):
    print("POG")
    if (tag in klass_lunch):
        print("Du får äta")
    else: 
        print("X")

