import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://www.aqistudy.cn/historydata/"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    page_text = response.text
    tree = etree.HTML(page_text)
    allCity = []
    # 愚蠢写法
    # allList = tree.xpath('//div[@class="bottom"]/ul')
    # for ul in allList:
    #     text_div = ul.xpath('./div')
    #     if text_div != []:
    #         text_div = text_div[1]
    #         li = text_div.xpath('./li')
    #         for text_li in li:
    #             text = text_li.xpath('./a/text()')[0]
    #             allCity.append(text)

    # 精简写法
    # allList = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
    # for ul in allList:
    #     text = ul
    #     allCity.append(text)

    # 联合写法
    # 热门城市
    # //div[@class="bottom"]/ul/li/a
    # 这里虽然路径不同，但都是获取a标签 通过|运算符将其放入一个集合
    allList = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a | //div[@class="bottom"]/ul/li/a')
    for ul in allList:
        text = ul.xpath('./text()')[0]
        allCity.append(text)
    print(allCity, len(allCity))
