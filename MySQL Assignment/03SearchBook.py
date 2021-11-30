import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

bcode=int(input('Enter BookCode to be search: ' ))
curs.execute('select * from Books where BookCode=%d' %bcode)
data=curs.fetchone()
print(data)


print('-'*50)
try:
    
    print('Book Code          : %d' %data[0])
    print('Book Name          : %s' %data[1])
    print('Book Category      : %s' %data[2])
    print('Book Author        : %s' %data[3])
    print('Book Publication   : %s' %data[4])
    print('Book Edition       : %d' %data[5])
    print('Book Price         : %.2f' %data[6])
except:
    print('Book does not exist in the data')

con.close()
