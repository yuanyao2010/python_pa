 #"https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}"

#"https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782252","need_bookinfo":1}"

import requests
import asyncio
import aiohttp
import json
import aiofiles

async def aiodownload(cid,b_id,title):
    data ={
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic =  await resp.json()
            async with aiofiles.open(title,mode="w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])
            

async def getCatalog(url):
   resp = requests.get(url)
   dic = resp.json()
   tasks = []
   for item in dic['data']['novel']['items']:
       title = item['title']
       cid = item['cid']
       tasks.append(asyncio.create_task(aiodownload(cid,b_id,title)))
       #print(cid,title)
       await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
    #getCatalog(url)
    asyncio.run(getCatalog(url))