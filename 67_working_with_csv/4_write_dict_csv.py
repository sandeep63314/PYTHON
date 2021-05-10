import csv

with open('grocery.csv',mode = 'r') as read_csv:
    csv_reader = csv.DictReader(read_csv)

    fieldnames = ['date_of_purchase','itemid','itemname','quantity','price']

    with open('newDictionarybill.csv','w') as write_csv:
        csv_writer = csv.DictWriter(write_csv,fieldnames = fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(csv_reader)