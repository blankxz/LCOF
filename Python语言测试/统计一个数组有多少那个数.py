print(len([i for i in [1,4,5,5,5,6,7,5] if i == 5]))

a= "S".encode("gbk").decode("utf-8",'ignore')
print(a)

# try:
#     print(c)
# except Exception as e:
#     print(e)
#     print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
#     print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数
import copy

a = [1,2]

b = a
c = a.copy()
d = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))
print(id(d))

a = (1,2)
b = (1,2)
print(id(a))
print(id(b))
c = copy.copy(a)
print(id(c))

dd = [1,2,3]
ddd = 1
print(id(dd))
def d(dd,ddd):
    ddd = 2
    print(id(dd))
    dd.append(1)
print(dd)
d(dd,ddd)
print(dd)
print(ddd)