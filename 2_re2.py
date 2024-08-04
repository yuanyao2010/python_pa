
import requests

domain = "https://www.dytt89.com"

Headers = {    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
resp = requests.get(url=domain,headers=Headers)
print(resp.text)
# 导入模块
# import requests

# # 请求头
# Headers = {    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',    'Referer': 'https://www.ygdy8.net/html/gndy/dyzz/index.html'}
# # 请求第一页
# One_Url = 'https://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
# Requ = requests.get(url=One_Url, headers=Headers)
# Text = Requ.content.decode('gbk')
# print(Text)