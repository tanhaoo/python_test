import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects'
    size = input('input size')
    start = input('input start')
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    param = {
        'type': 'movie',
        'tag': '经典',
        'sort': 'recommend',
        'page_limit': size,
        'page_start': start
    }
    response = requests.get(url, param, headers=headers)
    obj = response.json()
    print(obj)
    fp = open('./movie.json', 'w', encoding='UTF-8')
    json.dump(obj, fp=fp, ensure_ascii=False)
