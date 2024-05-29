#破解百度翻译
import requests
import json
if __name__ == "__main__":
    # 1、指定url
    post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    # 2、进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.76'
    }
    #3、post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'query':word
    }
    #4、请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5、获取响应数据；json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json())
    dic_obj = response.json()
    print(dic_obj)
    #持久化存储
    filename = word+'.json'
    fp=open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!!!')