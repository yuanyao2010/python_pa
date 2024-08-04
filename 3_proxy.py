import requests

proxies={
    "http":"http://183.234.215.11:8443"
}

resp = requests.get("http://www.baidu.com",proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)