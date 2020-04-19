import re

pattern = re.compile(r'(.*?)@(.*?).com')  # 查找数字
result = pattern.findall('你好993010776@qq.com')
print(result)