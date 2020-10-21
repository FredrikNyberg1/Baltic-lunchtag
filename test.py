import csv
import pandas as pd
import tkinter as tk

df = pd.read_csv('taggar.csv')

app = tk.Tk()

#Fullscreen
app.overrideredirect(True)
app.overrideredirect(False)
app.attributes('-fullscreen',True)

while True:
    tag = int(input("Input tag: "))

    i = 0

    klasser = df.columns

    tags = []


    for klass in klasser:
        #print(klasser[i])
        klass_tags = df[klasser[i]].to_list()
        #print(klass_tags)
        tags.extend(klass_tags)
        #print(tags)
        i += 1

    app.configure(bg='black')

    if (tag in tags):
        print("Ja")

        app.configure(bg='green')
        
    else: 
        print("Nej")
        app.configure(bg='red')

app.mainloop()