#coding=utf-8
import re

# 将正则编译成Pattern对象
pattern = re.compile(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(25[0-5]|2[0-4]\d(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$|1[0-9][0-9]|[1-9]?[0-9])$')

# re.match匹配文本，成功时返回match对象，失败时返回None
result1 = re.match(pattern, '192.1.25.255')

#  match对象的属性与方法
print result1.group()
