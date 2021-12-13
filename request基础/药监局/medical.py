import requests
import json

if __name__ == '__main__':
    # 标题页
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # 详情页
    url_1 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }

    # 获取1-5页ID
    for page in range(1, 6):
        id_list = []
        all_data_list = []
        param = {
            'on': True,
            'page': page,
            'pageSize': 15,
            'conditionType': 1,
        }
        json_ids = requests.post(url, param, headers=headers).json()
        for dic in json_ids['list']:
            # 标题ID
            id_list.append(dic['ID'])
        print(id_list)
        for id in id_list:
            detail_json = requests.post(url_1, {'id': id}, headers).json()
            all_data_list.append(detail_json)
        fp = open('allData_'+str(page)+'.json', 'w', encoding='UTF-8')
        json.dump(all_data_list, fp, ensure_ascii=False)
