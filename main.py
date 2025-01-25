import csv 

with open("temperatures.csv", "r") as file:
    temp_file = csv.reader(file)

    for row in temp_file:
        print(f"It is currently {row[1]} degrees and {row[2].lower()} in {row[0]}.")
