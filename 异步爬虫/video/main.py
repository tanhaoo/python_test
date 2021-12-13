import os.path
import random
import time

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool


def get_video_data(dic):
    name = dic['name']
    url = dic['url']
    print(name + "正在下载...")
    start = time.time()
    video_data = requests.get(url, headers=headers).content
    if not os.path.exists('./videos'):
        os.mkdir('./videos')
    with open('./videos/' + name, 'wb') as fp:
        fp.write(video_data)
        print(name + "下载成功", '耗时' + str(time.time() - start))


if __name__ == '__main__':
    url = "https://www.pearvideo.com/category_5"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    all_list = tree.xpath('//*[@id="listvideoListUl"]/li/div/a')
    urls = []
    for page in all_list:
        page_url = "https://www.pearvideo.com/" + page.xpath('@href')[0]
        page_name = page.xpath('./div[@class="vervideo-title"]/text()')[0] + '.mp4'
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "referer": page_url
            # 这里加上referer 然后下面get请求改发送post请求就能拿到数据
        }
        # print(page_url)
        ex = 'video_(.*)'
        video_id = re.findall(ex, page_url)[0]
        # print(video_id)
        video_request = "https://www.pearvideo.com/videoStatus.jsp"
        params = {
            'contId': video_id,
            # 'mrd': str(random.random())
        }
        # print(video_request, params)
        data = requests.post(video_request, headers=header, data=params).json()
        # print(data['videoInfo']['videos']['srcUrl'])
        # 源url做了伪装，需要二次处理才能拿到正确url
        video_url = data['videoInfo']['videos']['srcUrl']
        result = re.findall('/\d+/(.*?)-', video_url)[0]
        video_url = re.sub(result, 'cont-' + video_id, video_url)
        dic = {
            'name': page_name,
            'url': video_url
        }
        urls.append(dic)
        # print(video_url)
    print(urls)
    # 使用线程池对数据进行请求
    pool = Pool(4)
    pool.map(get_video_data, urls)
    pool.close()
    pool.join()
