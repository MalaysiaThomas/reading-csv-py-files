import csv 

with open("temperatures.csv", "r") as file:
    temp_file = csv.reader(file)

    for row in temp_file:
        print(row)