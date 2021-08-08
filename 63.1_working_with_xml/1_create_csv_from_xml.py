import xml.etree.ElementTree as et
import csv

##Start reading elements in a xml file
xmldoc = et.parse('country.xml')  # used for parsing a xml file
root = xmldoc.getroot()  # extract the root element from the xml file. If you are putting xml content in a string then use xmldoc.fromstring(xmltext) to extract the root element
# print(root.tag,root.attrib)  # extract the tag name of the root element
contents = []

for country in root:  # used to loop through child elements of root element
    det = {}
    for k, v in country.attrib.items():
        det.update({'countryname': v})
    for countrydetails in country:
        if countrydetails.attrib == {}:
            det.update({countrydetails.tag: countrydetails.text})
            continue
        else:
            rec = det.copy()
            for k, v in countrydetails.attrib.items():
                rec.update({k:v})
        det = rec
        contents.append(det)
##End reading contents in a xml file
fieldnames = ['countryname','rank','year','gdppc','name','direction','latitude']
with open('fromxml.csv', 'w', newline = '',encoding = 'utf-8') as csvwriter:
    writecsv = csv.DictWriter(csvwriter,fieldnames = fieldnames)
    writecsv.writeheader()
    writecsv.writerows(contents)
    print('Completed!!!')