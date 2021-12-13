import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://www.baidu.com/s?ie=utf-8&wd=ip"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(url, headers=headers, proxies={"http": '60.167.22.163:1133'})
    response.encoding = 'utf-8'
    page_text = response.text
    print(response.status_code)
    with open('./ip.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(page_text)
    tree = etree.HTML(page_text)
    ip = tree.xpath('//*[@id="results"]/div[1]/div[1]/article/section/div/div/div/div[1]/div/div/div[3]/div/div/div/div/div/div[2]/div[1]/div/div/span/text()')
    print(ip)
