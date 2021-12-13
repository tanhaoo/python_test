import ddddocr
import requests
from lxml import etree


def getCode(url, headers, session):
    page_text = session.get(url, headers=headers).text
    tree = etree.HTML(page_text)
    code_url = "https://so.gushiwen.cn/" + tree.xpath('//*[@id="imgCode"]/@src')[0]
    code_content = session.get(code_url, headers=headers).content
    ocr = ddddocr.DdddOcr()
    with open('./code.png', 'wb') as fp:
        fp.write(code_content)
    return ocr.classification(code_content)


if __name__ == '__main__':
    # 这里从获取图片验证码开始就用用一套session ，当用session发送post请求成功后，服务器会响应cookie，用session的话就会自动保存，
    # 然后再用这个session去请求个人主页，服务器就认为已经登录
    session = requests.Session()
    url = "https://so.gushiwen.cn/user/login.aspx"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    result = getCode(url, headers, session)
    print(result)

    data = {
        '__VIEWSTATE': 'zMqYpKdpur4B6/qNKK33DRrp3bTZt7a2hvylZPa4jOJDPIQFqix1ltB4jbqQYtEeLkA5mv6WrnEF5z0r5rJSaGz7Ua9W6/xI6e+Mdl5zfRIKkc/1WNBuis559j8=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '514787498@qq.com',
        'pwd': 'sjm2009123',
        'code': result,
        'denglu': '登录'
    }
    print(data)
    response = session.post(url, data=data, headers=headers)
    print(response.status_code)
    result_response_text = session.get("https://so.gushiwen.cn/user/collect.aspx", headers=headers).text
    with open('gushi.html', 'w', encoding='utf-8') as fp:
        fp.write(result_response_text)
    # //*[@id="imgCode"]
