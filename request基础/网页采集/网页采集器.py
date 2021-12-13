import requests

if __name__ == '__main__':
    url = "https://www.baidu.com/s"
    sogou_url = "https://www.sogou.com/web"
    kw = input('enter a word:')
    # UA伪装，为了让服务器认为这是一个浏览器发送的请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    param = {
        'ie': 'UTF-8',
        'wd': kw
    }
    sougou_param = {
        'query': kw
    }
    # response = requests.get(url, param, headers=headers)
    response = requests.get(sogou_url, sougou_param, headers=headers)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='UTF-8') as fp:
        fp.write(page_text)
    print(fileName, "保存成功！")
