import asyncio


async def others(id):
    print('start', id)
    await asyncio.sleep(id)
    print('end', id)
    return '我是返回值' + str(id)


async def func():
    print('main开始')
    task1 = asyncio.create_task(others(1))
    task2 = asyncio.create_task(others(2))
    print('执行协程函数1')
    response1 = await task1
    print('携程函数执行结束，结果为 ', response1)

    print('执行协程函数2')
    response2 = await task2
    print('协程函数执行结束，结果为 ', response2)

if __name__ == '__main__':
    asyncio.run(func())
