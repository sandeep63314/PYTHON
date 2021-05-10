import csv

with open('grocery.csv',"r") as read_csv:
    csv_reader = csv.DictReader(read_csv)

    for line in csv_reader:
        print(line)
