import os.path

import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://sc.chinaz.com/jianli/free.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    allList = tree.xpath('//div[@id="main"]/div/div/a')
    if not os.path.exists('./download'):
        os.mkdir('./download')
    for a in allList:
        url = "https:" + a.xpath('./@href')[0]
        name = a.xpath('./img/@alt')[0]
        page = requests.get(url, headers=headers).text
        tree = etree.HTML(page)
        download_url = tree.xpath('//ul[@class="clearfix"]/li/a/@href')[0]
        # rar也是二进制文件 用content拿
        download_content = requests.get(download_url, headers=headers).content
        download_path = 'download/' + name + '.rar'
        fp = open(download_path, 'wb')
        fp.write(download_content)
        print(name + " 下载完成")
