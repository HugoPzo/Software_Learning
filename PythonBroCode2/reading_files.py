# Python reading (.txt, .json, .csv)

import json
import csv


file_path = "C:/Users/hugop/OneDrive/Escritorio/output.json"

try:
    with open(file_path, "r") as file:
        # Read 'json'
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file doesn't exists")


file_path = "C:/Users/hugop/OneDrive/Escritorio/output.csv"


try:
    with open(file_path, "r") as file:
        # Read .csv
        content = csv.reader(file)
        for row in content:
            print(row)

except FileNotFoundError:
    print("That file doesn't exists")

