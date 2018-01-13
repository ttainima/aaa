from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from datetime import  timedelta
import random
import Conn
import pymysql
import paramiko
path="/usr/local/src/.ssh/task28"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("172.31.20.238",22,"root", "ay8u83d#2e@r5Dpy")
def tick():
    print (datetime.now())

def tick2(num,atime,kthe):
   sql = Conn.Conn.sql2
   mysqlconn = Conn.Conn.conn
   cursor = mysqlconn.cursor()
   query = (num,atime,kthe)
   cursor.execute(sql % query)
   mysqlconn.commit()
   aatime=atime.strftime("%Y-%m-%d %H:%M:%S")
   log=aatime+": "+"已开奖："+num
   logs="已有结果："+aatime+"----期数："+kthe+"，结果："+num
   stdin, stdout, stderr = ssh.exec_command("echo " +log+ ">>/home/git/gcopen/log/sfpk10_auto201712.log;echo " +logs+">>/home/git/gcopen/logs/三分PK拾201712.log")
   print("do")

if __name__ == "__main__":
    sche = BlockingScheduler()
    for line in open("/usr/local/src/.ssh/aaa/task","rt"):
        line = line.replace('\n',"")
        if(line==''):
            break
        aa = line.split('|')
        rint = random.randint(2,10)
        t_time = datetime.strptime(aa[1].strip(),'%Y-%m-%d %H:%M:%S')-timedelta(seconds=20)
        atime = datetime.strptime(aa[1].strip(),'%Y-%m-%d %H:%M:%S')-timedelta(seconds=rint)
        sche.add_job(tick2,'date',run_date=t_time.strftime( '%Y-%m-%d %H:%M:%S'),args=[aa[2],atime,aa[0]])
    sche.start()
