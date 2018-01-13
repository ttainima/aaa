import redis
import json
r = redis.Redis(host='xjpgc01redis.0gempi.ng.0001.apse1.cache.amazonaws.com',port=6379,db=8)
#r = redis.Redis(host='192.168.8.102',port=6379,db=8)
s1= open("d:\dsn.txt","rt")
s=""
for ss1 in s1:
    s=s+ss1
sj = json.loads(s)
sj2=json.dumps(sj)
for f in open("d:\domain.txt","rt"):
    if f.strip()=="":
        continue
    print(f)
    r.hset("dsn",f.strip(),sj2.strip())
