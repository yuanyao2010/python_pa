import requests
from bs4 import BeautifulSoup
url = "http://www.xinfadi.com.cn/priceDetail.html"
resp = requests.get(url)
print(resp.text)
