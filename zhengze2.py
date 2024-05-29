#需求：爬取头像网中所有的头像图片
import requests
import re
import os
if __name__ == '__main__':
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./touxiangLibs'):
        os.mkdir('./touxiangLibs')

    url = 'https://www.duitang.com/category/?cat=avatar'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url,headers=headers).text
    #使用聚焦爬虫将页面中所有的头像进行解析/提取
    ex = '<div class="mbpho" style.*?>.*?<img data-rootid.*? alt.*? data-iid.*? src="(.*?)" height.*?</div>'
    img_src_list = re.findall(ex,page_text,re.S)
    # print(img_src_list)
    for src in img_src_list:
        #请求到了图片的二进制数据
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name = src.split('/')[-1]
        #图片存储的路径
        imgPath = './touxiangLibs/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')
