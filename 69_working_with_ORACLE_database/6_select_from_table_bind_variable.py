import cx_Oracle

try:
    con = cx_Oracle.connect('sangram/sangram@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
    print('There is error in the Oracle database:' + str(er))

else:
    try:
        cur = con.cursor()

        cur.execute('select * from employee where salary > :sal', {'sal': 50000})
        rows = cur.fetchall()
        print(rows)

    except cx_Oracle.DatabaseError as er:
        print('There is error in the Oracle database:'+str(er))

    except Exception as er:
        print('Error:'+str(er))

    finally:
        if cur:
            cur.close()

finally:
    if con:
        con.close()