import csv

with open('grocery.csv','r') as read_csv:
    csv_reader = csv.reader(read_csv)

    with open('newbill.csv','w',newline='') as write_csv:
        csv_writer = csv.writer(write_csv,delimiter = ";") # to change the delimiter before writing to the new file
        csv_writer.writerows(csv_reader)
        # for line in csv_reader:
        #     csv_writer.writerow(line)