import requests
url = "https://www.umei.cc/bizhitupian/shoujibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)