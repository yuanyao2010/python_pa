import requests

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
print(resp.text)