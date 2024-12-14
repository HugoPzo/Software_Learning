# Python writing (.txt, .json, .csv)

import json


employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:/Users/hugop/OneDrive/Escritorio/output.json"

try:
    with open(file_path, "w") as file:
        # Convert dictionary to a 'json'
        json.dump(employee, file, indent=2)
        print(f"json file '{file_path}' was created")

except FileExistsError:
    print("That file already exists")


import csv

file_path = "C:/Users/hugop/OneDrive/Escritorio/output.csv"


employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]


try:
    with open(file_path, "w", newline="") as file:
        # Convert to a .csv
        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")


except FileExistsError:
    print("That file already exists")