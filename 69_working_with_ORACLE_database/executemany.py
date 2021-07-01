import cx_Oracle
import csv

# Load data from a csv file into Oracle table using executemany
try:
    con = cx_Oracle.connect('sangram/sangram@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
    print('There is an error in Oracle database:' + str(er))

else:
    try:
        cur = con.cursor()
        data = [{'id':10010, 'nm':'Vikram', 'sal':48000.0}, {'id':10011, 'nm':'Sunil', 'sal':65000.1}, {'id':10012, 'nm':'Sameer', 'sal':75000.0}]

        cur = con.cursor()
        # Inserting multiple records into employee table
        cur.executemany('insert into employee values(:id,:nm,:sal)', data)

    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)

    except Exception as er:
        print(er)

    else:
        # To commit the transaction manually
        print('Multiple records are inserted successfully')

finally:
    if cur:
        cur.close()
    if con:
        con.close()
