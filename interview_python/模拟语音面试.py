import win32com.client
import random
import time
 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
web_question = ['TCP 三次握手','为什么是三次握手而不是二次','TCP四次挥手','为什么连接的时候是三次握手，关闭的时候却是四次挥手？',
            'TCP超时重传','TCP滑动窗口','TCP的拥塞控制','TCP UDP的区别','SYN攻击原理','HTTP各个版本区别',
            'Http请求方式，请求头','HTTPS和HTTP的区别','SOCKET','Cookie、Session和Token','Token是什么','OSI七层模型是哪七层',
            '五层体系结构是哪五层','HTTP过程','HTTP请求过程','HTTPS过程','DNS过程','流量控制引发的死锁？怎么避免死锁的发生？',
            '什么是流量控制？流量控制的目的？','如何实现流量控制？','拥塞控制和流量控制的区别','HTTP的报文格式']

sys_question = ['进程的常见状态？以及各种状态之间的转换条件','进程同步','进程的通信方式有哪些？','死锁','死锁条件如何处理',
                '生产消费者','进程与线程的区别','进程和线程的定义和关系','并发','并行','通过多线程实现并发，并行','进程/线程间同步机制',
                '调度算法','页面置换算法','逻辑地址 Vs 物理地址 Vs 虚拟内存','同步和互斥的区别','什么是线程安全','同步与异步','守护、僵尸、孤儿进程的概念',
                '用户态和内核态的区别','为什么要有用户态和内核态？','批处理系统','交互式系统','进程同步']


db_question = ['1、为什么要使用数据库',
'2、什么是SQL？',
'3、什么是MySQL?',
'4、数据库三大范式是什么',
'5、mysql有关权限的表都有哪几个',
'6、MySQL的binlog有有几种录入格式？分别有什么区别？',
'1、mysql有哪些数据类型',
'1、MySQL存储引擎MyISAM与InnoDB区别',
'2、MyISAM索引与InnoDB索引的区别？',
'3、InnoDB引擎的4大特性',
'4、存储引擎选择',
'1、什么是索引？',
'2、索引有哪些优缺点？',
'3、索引使用场景（重点）',
'4、索引有哪几种类型？',
'5、索引的数据结构（b树，hash）',
'6、索引的基本原理',
'7、索引算法有哪些？',
'8、索引设计的原则？',
'9、创建索引的原则（重中之重）',
'10、创建索引的三种方式，删除索引',
'11、创建索引时需要注意什么？',
'12、使用索引查询一定能提高查询的性能吗？为什么',
'13、百万级别或以上的数据如何删除',
'14、前缀索引',
'15、什么是最左前缀原则？什么是最左匹配原则',
'16、B树和B+树的区别',
'17、使用B树的好处',
'18、使用B+树的好处',
'19、Hash索引和B+树所有有什么区别或者说优劣呢?',
'20、数据库为什么使用B+树而不是B树',
'21、B+树在满足聚簇索引和覆盖索引的时候不需要回表查询数据，',
'22、什么是聚簇索引？何时使用聚簇索引与非聚簇索引',
'23、非聚簇索引一定会回表查询吗？',
'24、联合索引是什么？为什么需要注意联合索引中的顺序？',
'1、什么是数据库事务？',
'2、事物的四大特性(ACID)介绍一下?',
'3、什么是脏读？幻读？不可重复读？',
'4、什么是事务的隔离级别？MySQL的默认隔离级别是什么？',
'1、对MySQL的锁了解吗',
'2、隔离级别与锁的关系',
'3、按照锁的粒度分数据库锁有哪些？锁机制与InnoDB锁算法',
'4、从锁的类别上分MySQL都有哪些锁呢？像上面那样子进行锁定岂不是有点阻碍并发效率了',
'5、MySQL中InnoDB引擎的行锁是怎么实现的？',
'6、InnoDB存储引擎的锁的算法有三种',
'7、什么是死锁？怎么解决？',
'8、数据库的乐观锁和悲观锁是什么？怎么实现的？',
'1、为什么要使用视图？什么是视图？',
'2、视图有哪些特点？',
'3、视图的使用场景有哪些？',
'4、视图的优点',
'5、视图的缺点',
'6、什么是游标？',
'1、什么是存储过程？有哪些优缺点？',
'1、什么是触发器？触发器的使用场景有哪些？',
'2、MySQL中都有哪些触发器？',
'1、SQL语句主要分为哪几类',
'2、超键、候选键、主键、外键分别是什么？',
'3、SQL 约束有哪几种？',
'4、六种关联查询',
'5、什么是子查询',
'6、子查询的三种情况',
'7、mysql中 in 和 exists 区别',
'8、varchar与char的区别',
'9、varchar(50)中50的涵义',
'10、int(20)中20的涵义',
'11、mysql为什么这么设计',
'12、mysql中int(10)和char(10)以及varchar(10)的区别',
'13、FLOAT和DOUBLE的区别是什么？',
'14、drop、delete与truncate的区别',
'15、UNION与UNION ALL的区别？',
'1、如何定位及优化SQL语句的性能问题？创建的索引有没有被使用到?或者说怎么才可以知道这条语句运行很慢的原因？',
'2、SQL的生命周期？',
'3、大表数据查询，怎么优化',
'4、超大分页怎么处理？',
'5、mysql 分页',
'6、慢查询日志',
'7、关心过业务系统里面的sql耗时吗？统计过慢查询吗？对慢查询都怎么优化过？',
'8、为什么要尽量设定一个主键？',
'9、主键使用自增ID还是UUID？',
'10、字段为什么要求定义为not null？',
'11、如果要存储用户的密码散列，应该使用什么字段进行存储？',
'12、优化查询过程中的数据访问',
'13、优化长难的查询语句',
'14、优化特定类型的查询语句',
'15、优化关联查询',
'16、优化子查询',
'17、优化LIMIT分页',
'18、优化UNION查询',
'19、优化WHERE子句',
'1、为什么要优化',
'2、数据库结构优化',
'3、MySQL数据库cpu飙升到500%的话他怎么处理？',
'4、大表怎么优化？某个表有近千万数据，CRUD比较慢，如何优化？分库分表了是怎么做的？分表分库了有什么问题？有用到中间件么？他们的原理知道么？',
'4、垂直分表适用场景，缺点，水平分表：适用场景，水平切分的缺点',
'5、MySQL的复制原理以及流程',
'6、读写分离有哪些解决方案？',
'7、备份计划，mysqldump以及xtranbackup的实现原理',
'8、数据表损坏的修复方式有哪些？']

while 1:
    question_type = [web_question,sys_question,db_question]
    question = random.choice(question_type)
    words = '请说一下'+random.choice(question)
    print(words)
    speaker.Speak(words)
    input()