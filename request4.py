#需求：爬取豆瓣电影分类排行榜中的电影详情数据
import requests
import json
if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    param ={
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '1',
        'limit': '20',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.76'
    }
    response = requests.get(url=url,params=param, headers=headers)
    # print(response.text)
    list_data = response.json()
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!!!')