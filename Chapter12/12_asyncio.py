import asyncio

"""
asyncio 是用来编写 并发 代码的库，使用 async/await 语法。
asyncio 被用作多个提供高性能 Python 异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。

asyncio 往往是构建 IO 密集型和高层级 结构化 网络代码的最佳选择。
"""
# async def compute():
# 	for i in range(5):
# 		print('compute %d' % i)
# 		await asyncio.sleep(.1)

# async def compute2():
# 	for i in range(5):
# 		print('compute2 %d' % i)
# 		await asyncio.sleep(.2)

# async def main():
# 	await asyncio.gather(compute(), compute2())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())