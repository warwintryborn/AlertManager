from os import getenv
import pymssql

conn = pymssql.connect(server='172.16.1.96', user='sa', password='evt!123456', database='WF_Utilidades')
cursor = conn.cursor()

cursor.execute('SELECT * FROM listaNaoAtendidosQtde')

print( cursor.fetchall() )

conn.close()

