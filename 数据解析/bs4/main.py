from bs4 import BeautifulSoup
import requests

# pip install lxml
# pip install bs4
if __name__ == '__main__':
    # page_text = response.text
    # soup = Beautiful(page_text,'lxml')
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    text = response.text
    soup = BeautifulSoup(text, 'lxml');
    # li_list = soup.select('.book-mulu > ul > li')
    li_list = soup.select('.book-mulu li')
    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.text
        title_url = 'https://www.shicimingju.com' + li.a['href']
        response = requests.get(title_url, headers=headers)
        response.encoding = 'utf-8'
        title_request_text = response.text
        soup = BeautifulSoup(title_request_text, 'lxml')
        title_text = soup.find('div', class_='chapter_content').text
        # title_text = soup.select('.chapter_content')[0].text
        # 因为用select返回的是数组，又不想用find，就用这种方式获得文本
        fp.write(title + ':' + title_text + '\n')
        print(title + ' 下载完成')
