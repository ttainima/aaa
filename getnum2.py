import pymysql
from Conn import Conn
sql = Conn.sql4
myconn = Conn.conn
corsor = myconn.cursor()
corsor.execute(sql)
for data in corsor.fetchall():
    print(data[3],end='|')
    print(data[4])

