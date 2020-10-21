import csv
import pandas as pd
from datetime import datetime, time, date

tid = datetime.now().time()
datum = datetime.now().date()
dag = datetime.now().weekday()

print(tid)
print(dag)

taggar_csv = pd.read_csv('taggar.csv')
schema_csv = pd.read_csv('schema.csv')

i = 0

klasser = taggar_csv.columns
tider = schema_csv.columns
# dagar = schema_csv.iloc[]


# print(dagar)

tags = []

klass_lunch = []

# for klass in klasser:
#     # print(klasser[i])
#     klass_tags = taggar_csv[klasser[i]].to_list()
#     # print(klass_tags)
#     tags.extend(klass_tags)
#     # print(tags)
#     i += 1

i = 0




lunchdag = schema_csv.iloc[dag, 0]
print(lunchdag)
tag = int(input("Input tag: "))

# for tag in tags:


#         print("Du får äta nu!")
#     else:
#         print("Du får inte äta nu")
                
# if (tag in klass_Na20):
#     if (tid > tid.replace(hour=11, minute=0, second=0, microsecond=0)):
#         print("Du får äta nu")
#     else:
#         print("Du får inte äta nu.mp3")