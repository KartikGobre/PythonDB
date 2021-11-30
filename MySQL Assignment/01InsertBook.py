import mysql.connector

con=mysql.connector.connect(host='bspfbttwbghulecudnz2-mysql.services.clever-cloud.com',user='ur4ny43q3uciwc1b',password='iHJmWL2bnoXjeog3LdRm',database='bspfbttwbghulecudnz2')
curs=con.cursor()

try:
    bcode=int(input('Enter Book Code: '))
    bnm=input('Enter Book Name: ')
    cat=input('Enter Book Category: ')
    aut=input('Enter Author Name: ')
    publ=input('Enter Publication Name: ')
    edt=int(input('Enter Edition Number: '))
    prc=float(input('Enter Book Price: '))      
    curs.execute("insert into Books values(%d, '%s', '%s', '%s', '%s', %d, '%.2f')" %(bcode,bnm,cat,aut,publ,edt,prc))
    con.commit()
    print('New Book inserted successfully')
    
    
    
except:
    print('Invalid input... cant insert the book')

con.close()
