import requests
query = input("请输入一个明星")

url = f'https://www.sogou.com/web?query={query}'



# url = 'https://www.sogou.com/web?query=周杰伦'

dic = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=dic)

print(resp)
print(resp.text)