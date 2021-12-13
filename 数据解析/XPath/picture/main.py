import os.path

import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://pic.netbian.com/4kmeinv/"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    # 解决中文乱码问题 方案1 要么试 utf-8 要么 gbk
    # response.encoding = 'gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    allList = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./pictures'):
        os.mkdir('./pictures')
    for li in allList:
        # xpath永远返回集合
        name = li.xpath('./a/b/text()')[0] + '.jpg'
        # 解决中文乱码问题 方案2
        name = name.encode('iso-8859-1').decode('gbk')
        url = "https://pic.netbian.com" + li.xpath('./a/img/@src')[0]
        img_data = requests.get(url, headers=headers).content
        img_path = 'pictures/' + name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(name + ' 下载成功')
