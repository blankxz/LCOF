import win32com.client
import random
import time
 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
web_question = ['TCP 三次握手','为什么是三次握手而不是二次','TCP四次挥手','为什么连接的时候是三次握手，关闭的时候却是四次挥手？',
            'TCP超时重传','TCP滑动窗口','TCP的拥塞控制','TCP UDP的区别','SYN攻击原理','HTTP各个版本区别',
            'Http请求方式，请求头','HTTPS和HTTP的区别','SOCKET','Cookie、Session和Token','Token是什么','OSI七层模型是哪七层',
            '五层体系结构是哪五层','HTTP过程','HTTP请求过程','HTTPS过程','DNS过程','流量控制引发的死锁？怎么避免死锁的发生？',
            '什么是流量控制？流量控制的目的？','如何实现流量控制？','拥塞控制和流量控制的区别','HTTP的报文格式']

sys_question = ['进程的常见状态？以及各种状态之间的转换条件','进程同步','线程同步','进程的通信方式有哪些？','死锁','死锁条件如何处理',
                '生产消费者','进程与线程的区别','进程和线程的定义和关系','并发','并行','通过多线程实现并发，并行','进程/线程间同步机制',
                '调度算法','页面置换算法','逻辑地址 Vs 物理地址 Vs 虚拟内存','同步和互斥的区别','什么是线程安全','同步与异步','守护、僵尸、孤儿进程的概念',
                '用户态和内核态的区别','为什么要有用户态和内核态？']

while 1:
    question_type = [web_question,sys_question]
    question = random.choice(question_type)
    words = '请说一下'+random.choice(question)
    print(words)
    speaker.Speak(words)
    input()