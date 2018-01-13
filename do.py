import Conn
import pymysql
mysqlconn = Conn.Conn.conn
cursor = mysqlconn.cursor()
query = ('201711010019',)
sql = Conn.Conn.sql

cursor.execute(sql % query)
for row in cursor.fetchall():
    print(row[3])