import csv

content = [{'itemid':100,'itemname':'rice','price':45},
           {'itemid':101,'itemname':'dal','price':110},
           {'itemid':102,'itemname':'soyabean','price':80}
           ]

fieldnames = ['itemid','itemname','price','discount','quantity_unit']

with open('custom_dict_write.csv','w',newline='') as write_csv:
    csv_writer = csv.DictWriter(write_csv,fieldnames = fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(content)