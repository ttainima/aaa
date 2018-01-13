import pymysql
class Conn:
    conn = pymysql.connect(host='xjpgcbase01.ciasiaddtzq2.ap-southeast-1.rds.amazonaws.com',
    #conn = pymysql.connect(host='192.168.8.102',
    port=3306,
    user='root',
    passwd='kWln94we2P3R3',
    db='gc_base',
    charset='utf8' )
    sql = "select * from gc_open_num where kithe= '%s' and gid=27"
    sql2 = "UPDATE gc_open_num SET number = '%s',status=2,actual_time='%s' WHERE kithe = '%s' and status=1 and number='' and gid=27"
    sql3 = "select * from gc_open_num where open_time>'2018-01-08 00:00:00' and open_time<'2018-01-09 03:30:00' and gid=27 and status=1 and number=''"
    sql4 = "select * from gc_open_num where open_time>'2017-09-04 11:00:30' and open_time<'2017-11-24 14:00:00' and gid=27"

    sql5 = "UPDATE gc_open_num SET number = '%s',status=2,actual_time='%s' WHERE kithe = '%s' and status=1 and number='' and gid=24"
    sql6 = "select * from gc_open_num where open_time>'2018-01-02 00:00:01' and open_time<'2018-01-02 06:00:00' and gid=24 and status=1 and number=''"
    sql7 = "select * from gc_open_num where open_time>'2017-09-04 11:00:30' and open_time<'2017-11-04 14:00:00' and gid=24"
