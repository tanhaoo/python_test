import re
import requests
import os

if __name__ == '__main__':
    if not os.path.exists('./pic'):
        os.mkdir('./pic')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    url = 'https://www.qiushibaike.com/imgrank'

    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

    # .text 返回文本 .content 返回二进制 .json 返回json
    page_text = requests.get(url, headers=headers).text
    # 使用聚焦爬虫解析页面
    # .*? 非贪心匹配 就匹配一次 .* 贪心匹配 匹配尽可能多
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        # 图片url
        src = 'https:' + src
        img_data = requests.get(src, headers=headers).content
        # https://pic.qiushibaike.com/system/pictures/12482/124820544/medium/DYOAND21L339BRU2.jpg
        img_name = src.split('/')[-1]
        imgPath = './pic/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img_data)
            print(img_name + " 下载成功")
