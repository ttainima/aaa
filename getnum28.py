import pymysql
from Conn import Conn
sql = Conn.sql6
myconn = Conn.conn
corsor = myconn.cursor()
corsor.execute(sql)
for data in corsor.fetchall():
    print(data[2],end='|')
    print(data[3])