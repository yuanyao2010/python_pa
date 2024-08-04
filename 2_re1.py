import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=headers)
print(resp.text) 
page_content = resp.text
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>',re.S)
result = obj.finditer(page_content)
f = open("data.csv",mode="w",encoding="utf-8")
csvwriter = csv.writer(f)
for it in result:
#    print(it.group("name"))
#    print(it.group("score"))
#    print(it.group("num"))
#    print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over")