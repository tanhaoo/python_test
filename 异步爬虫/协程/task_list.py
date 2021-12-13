import asyncio
import time


async def others(id):
    print('start', id)
    await asyncio.sleep(id)
    print('end', id)
    return '我是返回值' + str(id)


def callback_func(task):
    print(task)


async def main():
    start =time.time()
    print('main开始')
    t1 = asyncio.create_task(others(1), name='t1')
    # 添加回调函数绑定到任务对象中
    t1.add_done_callback(callback_func)
    t2 = asyncio.create_task(others(2), name='t2')
    t2.add_done_callback(callback_func)
    task_list = [
        t1, t2
    ]
    done, pedding = await asyncio.wait(task_list, timeout=None)
    print('main结束')
    print(time.time()-start)
    # print(done)
    # for set in done:
    # print(set.result())

if __name__ == '__main__':
    asyncio.run(main())
