from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://sh.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    page_text = requests.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    first_list = tree.xpath('//section[@class="list"]')[0]
    all_list = first_list.xpath('./div')
    fp = open('58.txt', 'w', encoding='utf-8')
    for list in all_list:
        url = list.xpath('./a/@href')[0]
        name = list.xpath('.//h3/text()')[0]
        fp.write(name + '\n' + url + '\n\n')
        print(name)
