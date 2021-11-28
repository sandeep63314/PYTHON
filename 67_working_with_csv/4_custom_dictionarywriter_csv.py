import csv

content = [{'itemid':100,'itemname':'rice','price':45},
           {'itemid':101,'itemname':'dal','price':110},
           {'itemid':102,'itemname':'soyabean','price':80}
           ]

# fieldnames = ['itemid','itemname','price','discount','quantity_unit']
#
# with open('custom_dict_write.csv','w',newline='') as write_csv:
#     csv_writer = csv.DictWriter(write_csv,fieldnames = fieldnames)
#     csv_writer.writeheader()
#     csv_writer.writerows(content)

for c in content:
    if c['itemid'] == 100:
        c['quantity_unit'] = 2
        c['discount'] = '5%'
        c['totalprice'] = ((100 - eval(c['discount'].rstrip('%')))/100) * c['quantity_unit'] * c['price']
    if c['itemid'] == 101:
        c['quantity_unit'] = 3
        c['discount'] = '3%'
        c['totalprice'] = ((100 - eval(c['discount'].rstrip('%')))/100) * c['quantity_unit'] * c['price']
    if c['itemid'] == 102:
        c['quantity_unit'] = 5
        c['discount'] = '7%'
        c['totalprice'] = ((100 - eval(c['discount'].rstrip('%')))/100) * c['quantity_unit'] * c['price']

print(content)

fieldnames = ['itemid','itemname','price','quantity_unit','discount','totalprice']

with open('custom_dict_write.csv','w',newline='') as write_csv:
    csv_writer = csv.DictWriter(write_csv,fieldnames = fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(content)

