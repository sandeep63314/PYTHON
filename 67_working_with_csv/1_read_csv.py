import csv
import os

with open(os.path.abspath('C:\\users\\lenovo\\desktop\\PYTHON\\67_working_with_csv\\grocery.csv'),mode = "r") as read_csv:
    csv_reader = csv.reader(read_csv)

    for line in csv_reader:
        print(line)