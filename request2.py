#输入相关信息，爬取搜狗浏览器响应的网址
import requests
if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.76'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')