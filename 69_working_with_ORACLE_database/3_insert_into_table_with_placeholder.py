# importing module
import cx_Oracle

# Inserting a record into a table in Oracle database
try:
    con = cx_Oracle.connect('sangram/sangram@localhost:1521/xe')
    cursor = con.cursor()

    # To commit a transaction automatically
    con.autocommit = True

    id, nm, sal = 10003, 'Soumik', 30000.25
    # Inserting a record into table employee
    cursor.execute('insert into employee values(:1,:2,:3)',[id,nm,sal])

    print('Record inserted successfully')

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()