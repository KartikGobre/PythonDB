import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

try:
    bcode=int(input('Enter BookCode to be search: ' ))
    prc=float(input('Enter price (negative to reduce price): '))
    curs.execute('select * from Books where BookCode=%d' %bcode)
    data=curs.fetchall()
    if data:      
        curs.execute("update Books set price=price+%.2f where Bookcode=%d" %(prc,bcode))
        con.commit()
        print('Price updated successfully')
    else:
        print('Book does not exist')
except:
    print('Error in updating price')

con.close()