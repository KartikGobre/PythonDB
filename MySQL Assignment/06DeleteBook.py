import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

try:

    bcode=int(input('Enter Bookcode: '))
    curs.execute('select * from Books where Bookcode=%d' %bcode)
    data=curs.fetchall()
    if data:
        print(data)
        ask=input('Do you want to delete this Book ? ')
        if ask.lower()=="yes":
            curs.execute('delete from Books where Bookcode=%d' %bcode)
            con.commit()
            print('Book deleted successfully')
        else:
            print('OK')
    
    if not data:
        print('Book not found')
except:
    print('Error in deletion')
con.close()    