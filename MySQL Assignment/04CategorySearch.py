import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

cat=input('Enter Category to be search: ')
curs.execute("select * from Books where Category='%s'" %cat)
data=curs.fetchall()

        
print(data)
print('-'*100)
print('Total Books of Category "Romance" in Dataset: ',len(data))

con.close()