import csv
import pandas as pd
import time


# with open("taggar.csv", encoding='utf-8-sig') as file:
        # # Loops through tag file
    # for tag in reader:
tag = input("Input tag: ")

tags = []
df = pd.read_csv('taggar.csv')

# print(df)
if tag in df:
    # [Rad, Col]
    # print(df.iloc[tag])
    # print(df.columns)
    print("pog")
else:
    print("ERROR")