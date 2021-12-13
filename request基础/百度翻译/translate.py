import requests
import json

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    word = input('enter a word')
    response = requests.post(post_url, {'kw': word}, headers=headers)
    dic_obj = response.json()
    fp = open('./'+word+'.json', 'w', encoding='UTF-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print(dic_obj)
