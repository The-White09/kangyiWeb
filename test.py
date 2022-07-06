import pymysql
import time
import datetime

t = time.strptime('2020-12-7 13:52:15', "%Y-%m-%d %H:%M:%S")
nowt = time.strftime("%Y-%m-%d %H:%M:%S", t)
dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dt = str(dt)
print(dt)
print(isinstance(dt, str))
print(f"""{dt}""")
print("2022-07-06 17:19:34")
db = pymysql.connect(host='localhost',
                     user='root',
                     password='authMySQLhh@770425zxd',
                     database='zhkydb')
data = 1
call = 93
name = "sss"
realname = "sss"
pwd = "sss"
age = 23
ID = "ds"
address = "dw"
telephone = "13"
sql = """insert into sys_call(sys_call_id, sys_call_time, sys_call_type, sys_call_status, sys_call_old_id)VALUES({call}, "dt", 1, "waiting", {data});"""
sql1 = "INSERT INTO sys_call \
       VALUES ('%d', '%s',  %d,  '%s',  %d)" % \
       (call, dt, 20, 'M', 1)
cursor = db.cursor()
cursor.execute(sql1)
db.commit()
db.close()
