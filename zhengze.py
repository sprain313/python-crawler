#需求：爬取头像网中图片数据
import requests
if __name__ == "__main__":
    #如何爬取图片数据
    url = 'https://c-ssl.duitang.com/uploads/blog/202201/23/20220123222213_2899a.jpeg'
    #content返回的是二进制形式的图片数据
    #text（字符串） content（二进制） json（）（对象）
    img_data = requests.get(url=url).content
    with open('./touxiang.jpg','wb') as fp:
        fp.write(img_data)
    #
    #     聚焦爬虫：爬取页面中指定的页面内容。
    #     -编码流程：
    #     -指定url
    #     -发起请求
    #     -获取响应数据
    #     -数据解析
    #     -持久化存储
    # 数据解析分类：
    # -正则
    # -bs4
    # -xpath
    # 数据解析原理概述:
    # -解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
    # -1、进行指定标签的定位
    # -2、标签或者标签对应的属性中存储的数据值进行提取（解析）