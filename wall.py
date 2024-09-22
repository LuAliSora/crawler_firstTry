import urllib.request as request
import requests
import json

'''
@author:Lancer Wu
@email:wxs231@163.com
'''


def proxies_spider(canshu):
    '''
    使用代理的爬虫
    :param canshu: 用字典包裹的参数
    canshu = {
        'url': 'url',
        'cookie': 'cookie',
        ……
    }
    :return:
    '''

    # 代理设置
    proxies = {
        'https': 'https://127.0.0.1:64708',  # 查找到你的vpn在本机使用的https代理端口
        'http': 'http://127.0.0.1:64708',  # 查找到vpn在本机使用的http代理端口
    }

    # 请求的链接
    url = canshu['url']

    # 请求的参数
    data = {
        'canshu1': canshu['canshu1'],
        'canshu2': canshu['canshu2'],
        'canshu3': canshu['canshu3']
    }

    # 请求的头部
    headers = {
        'user-agent': user_agent,  # 全局变量
        'Cookie': canshu['cookie']  # 有需要则传入cookie
    }

    # request增加代理设置
    opener = request.build_opener(request.ProxyHandler(proxies))
    request.install_opener(opener)

    # get请求
    req_result = requests.get(url=url, params=data, headers=headers, proxies=proxies)

    # post请求
    # req_result = requests.post(url=url, data=data, headers=headers, proxies=proxies)

    # 如果是html页面：
    req_result = req_result.text

    # 如果是json数据：
    # req_result = req_result.json()

    return req_result


if __name__ == "__main__":
    # 访问的浏览器信息
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/56.0.2924.87 Safari/537.36'

    canshu = {
        'url': '',  # 请求的链接
        'cookie': '',  # 请求的cookie，如果不需要可以留空
        'canshu1': 'data1',  # 请求的第一个参数
        'canshu2': 'data2',  # 请求的第二个参数
        'canshu3': 'data3'  # 请求的第三个参数
    }

    # 提交查询
    req_result = proxies_spider(canshu)
    print('req_result', req_result)
