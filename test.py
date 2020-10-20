import csv
import pandas as pd
from datetime import datetime, time, date

tid = datetime.now().time()
datum = datetime.now().date()
dag = datum.strftime("%A")

print(tid)

df = pd.read_csv('taggar.csv')
dl = pd.read_csv('schema.csv')

# tag = int(input("Input tag: "))

i = 0

klasser = df.columns
tider = dl.columns

tags = []

klass_Ek20 = df[klasser[0]].to_list()
klass_Na20 = df[klasser[1]].to_list()

print(dl[tider[0]].to_list())



klass_lunch = []


for klass in klasser:
    # print(klasser[i])
    klass_tags = df[klasser[i]].to_list()
    # print(klass_tags)
    tags.extend(klass_tags)
    # print(tags)
    i += 1



if (tid >= dl[tider[0]].to_list()):
    print("Burh")
    
#     if (tag in klass_Na20):
#         print("Du får äta nu")
#     else:
#         print("Du får inte äta nu.mp3")

# if (tag in klass_Na20):
#     if (tid > tid.replace(hour=11, minute=0, second=0, microsecond=0)):
#         print("Du får äta nu")
#     else:
#         print("Du får inte äta nu.mp3")