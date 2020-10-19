import csv

with open("tags_20201012.csv", encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        # Loops through tag file
        for tag in reader:
            # Revomes brackets and quotations
            tag = "".join(tag)
            print(tag)