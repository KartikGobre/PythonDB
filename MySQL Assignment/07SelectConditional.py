import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

try:
    aut=input('Enter Author Name: ')
    publ=input('Enter Publication Name: ')

    curs.execute("select * from Books where Author='%s' and Publication='%s' " %(aut,publ))
    data=curs.fetchall()
    if data:
        print(data)
    else:
        print('Book not found')
except:
    print('Error in finding match')