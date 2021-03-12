import pyodbc

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=lenovo-PC;"
                      "Database=AdventureWorks2012;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()
cursor.execute("select * from dbo.department")

_myfile = open('dbcontent.txt', mode ='w')

for rows in cursor:
    _myfile = open('dbcontent.txt', mode='a')
    _myfile.write(str(rows[0])+','+str(rows[1]))
    _myfile.write('\n')

print('Database contents are written successfully.')