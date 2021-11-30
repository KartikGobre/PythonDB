import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()


try:
    bcode=int(input('Enter BookCode: '))
    curs.execute('select * from Books where BookCode=%d' %bcode)
    
    data=curs.fetchall()
    
    if data:
        rev=input('Review: ')
        curs.execute("update Books set Review='%s' where BookCode=%d" %(rev,bcode))
        con.commit()
        print('Review wrote successfully')
    else:
        print('Book not found')
except:
    print('Error in updating review')
