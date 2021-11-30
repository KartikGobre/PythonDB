import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',username='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()


try:
    curs.execute('alter table Books add Review varchar(500)')
    con.commit()
    print('Column Review altered in the table Books')
    con.close()
except:
    print('Column not altered in the table Books')





