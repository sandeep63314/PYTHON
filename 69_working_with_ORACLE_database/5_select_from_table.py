import cx_Oracle

try:
    con = cx_Oracle.connect('sangram/sangram@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
    print('There is an error in the Oracle database:', er)

else:
    try:
        cur = con.cursor()

        # fetchall() is used to fetch all records from result set
        cur.execute('select * from employee')
        rows = cur.fetchall()
        print(rows)

        # fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
        cur.execute('select * from employee')
        rows = cur.fetchmany(3)
        print(rows)

        # fetchone() is used fetch one record from top of the result set
        cur.execute('select * from employee')
        rows = cur.fetchone()
        print(rows)

    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:', er)

    except Exception as er:
        print('Error:'+str(er))

    finally:
        if cur:
            cur.close()

finally:
    if con:
        con.close()