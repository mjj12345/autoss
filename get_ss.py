import requests
import base64
import re
import time

today = time.strftime('%d',time.localtime(time.time()))
url = 'https://fastlink.ws/link/fg8nrb5omoirlffj?sub=2'

# 节点名称
name = '%E5%AD%A6%E6%9C%AF%E7%BA%BF%E8%B7%AF----{}%E5%8F%B7%E6%9B%B4%E6%96%B0'.format(today)
result = requests.get(url).text
#print(result)
result = base64.b64decode(result)
result_str = str(result,"utf-8")
with open("ss_temp.txt","w") as f:
    f.write(result_str)  # 自带文件关闭功能，不需要再写f.close()
with open("ss_temp.txt", "r") as f:
    data = f.readlines()
    #print(data)
    f.close()
a = ''
for i in data:
    #print(i.strip())
    pattern = re.compile(r'(ss.*)#')
    #str = u''
    m = pattern.match(i)
    #print(m[1]+'#{}'.format(name))
    a += m[1]+'#{}\n'.format(name)

bs = str(base64.b64encode(a.encode("utf-8")), "utf-8")

with open("ss.txt","w") as f:
    f.write(bs)  # 自带文件关闭功能，不需要再写f.close()
