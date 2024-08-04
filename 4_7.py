import asyncio
import aiohttp

urls =[
    "https://www.umei.cc/d/file/20230904/575ce4ac0259203a8cdb367ba889d814.jpg",
    "https://www.umei.cc/d/file/20230904/5d3d5bccb59cd791671e199c7a9d5d6e.jpg",
    "https://www.umei.cc/d/file/20230904/1f1d0637e436d276c5ac4a523c5052a7.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name,mode="wb") as f:
                f.write(await resp.content.read()) 
    print(name,"搞定")
async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())