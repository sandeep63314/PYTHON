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
        with open('employee.csv', 'r') as read_csv:
            csv_reader = csv.reader(read_csv)
            # Remove the header
            # Creating a list of records to be inserted into Oracle table
            csv_reader = list(csv_reader)[1:]
            # Data transformation within each record
            csv_reader = [[int(csv_reader[i][0]), csv_reader[i][1], float(csv_reader[i][2])] for i in
                          range(len(csv_reader))]

            cur = con.cursor()
            # Inserting multiple records into employee table
            cur.executemany('insert into employee values(:1,:2,:3)', csv_reader)

    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:' + str(er))

    except Exception as er:
        print(er)

    else:
        # To commit the transaction manually
        con.commit()
        print('Multiple records are inserted successfully')

finally:
    if cur:
        cur.close()
    if con:
        con.close()