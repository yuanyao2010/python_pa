
import time
import asyncio
# async def func():
#     print("你好好")

# if __name__ == '__main__':
#     g = func()
#     #print(g)
#     asyncio.run(g)

# async def func1():
#     print("你好啊,我叫pan")
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("你好啊,我叫pan")

# async def func2():
#     print("你好啊,我叫wan")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊,我叫wan")

# async def func3():
#     print("你好啊,我叫li")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好啊,我叫li")

# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [
#         f1,f2,f3
#     ]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)

# async def main():
#     # f1 = func1()
#     # await f1
#     tasks =[
#         func1(),
#         func2(),
#         func3()
#     ]
#     await asyncio.wait(tasks)

# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2-t1)

async def download(url):
    print("开始下载")
    asyncio.sleep(2)
    print("下载完成")

async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.163.com",
        "http://www.sohu.com"
    ]
    tasks = []
    for url in urls:
        d = asyncio.create_task(download(url))
        tasks.append(d)
    await asyncio.wait(tasks)
if __name__ == '__main__':
    asyncio.run(main())