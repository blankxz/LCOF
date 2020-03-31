import pymysql
import random
conn = pymysql.connect('localhost','root','123456','test1')

cursor = conn.cursor()

for i in range(1000):
    sql = 'insert into test4(id,a,b,c)values({},{},{},{})'.format(random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000))
    print(sql)
    cursor.execute(sql)

    # 涉及写操作要注意提交
    conn.commit()
conn.close()