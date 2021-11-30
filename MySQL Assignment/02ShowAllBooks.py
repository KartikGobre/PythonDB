import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

curs.execute('select * from Books')
data=curs.fetchall()
print(data)

for rec in data:
    print('Book Code          : %d' %rec[0])
    print('Book Name          : %s' %rec[1])
    print('Book Category      : %s' %rec[2])
    print('Book Author        : %s' %rec[3])
    print('Book Publication   : %s' %rec[4])
    print('Book Edition       : %d' %rec[5])
    print('Book Price         : %.2f' %rec[6])
    print('-'*50)

con.close()