import pymysql
import random
# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "countdb")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
for i in range(1000000):
    ip = '192.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    speed = random.randint(1,200)
    name = random.choice(['forever','yesterday','hello','good','perfect','fuck'])
    sql = 'INSERT INTO w10test(nam,ip,speed)values("{}","{}",{})'.format(name,ip,speed)
    cursor.execute(sql)
    print(i,ip)
db.commit()
# 关闭数据库连接
db.close()