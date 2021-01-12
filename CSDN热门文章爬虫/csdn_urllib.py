# -*- coding: utf-8 -*-
import urllib.request as ur
import urllib.parse as up
import lxml.etree as le
import re
from faker import Factory

# url = 'https://so.csdn.net/so/search/s.do?p={page}&q={keyword}&t=blog&viparticle=&domain=&o=&s=&u=&l=&f=&rbg=0'
url = 'https://so.csdn.net/so/search/all'
user_agent = Factory.create()


def getResponse(url, keyword, page):
    dict = {'q': keyword, 'p': page, 't': 'all', 's': 0, 'tm': 0, 'lv': -1, 'ft': 0}
    data = up.urlencode(dict).encode('utf-8')
    req = ur.Request(
        url=url,
        data=data,
        headers={
            'User-Agent': user_agent.user_agent()
            # 'User-Agent':'Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 5.01; Trident/5.1)',
            # 'Mozilla/5.0 (Windows NT 5.01) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/31.0.883.0 Safari/534.0'
        },
        method='GET'
    )
    # 【字符串对象】= 【字节对象】.decode('utf‐8','ignore')
    # 这个时候 response就是一个字符对象 ，保存的时候就不可以用wb
    response = ur.urlopen(req).read().decode('utf-8')
    # print(response)
    print(user_agent.user_agent())
    return response


if __name__ == '__main__':
    # keyword = input('关键词')
    # pn_start = int(input('起始页'))
    # pn_end = int(input('终止页'))
    keyword = 'python'
    pn_start = 1
    pn_end = 1

    # 中文操作
    data = up.urlencode(
        {'q': keyword}
    )
    print(keyword)

    for page in range(pn_start, pn_end + 1):
        # 访问1级页面
        response = getResponse(url=url, page=page, keyword=data)
        print(response)
        # 二级页面，博客的链接
        with open('1.html', 'w', encoding='utf-8') as f:
            f.write(response)
        hrefs = le.HTML(response).xpath(
            '//dl[@class="search-list J_search"]/a/@href')  # //span[@class="mr16"]/../../dt/div/a[1]/@href
        # 遍历二级页面
        print(hrefs)
        for href in hrefs:
            response_blog = getResponse(
                url=href,
            )
            # 文件名称
            title = le.HTML(response_blog).xpath('//h1[@class="title-article"]/text()')[0]
            # 文件名称除去非法字符
            title = re.sub(
                r'[/\\:*"<>|? ]', '', title
            )
            # 文件路径
            filepath = 'blog/%s.html' % title
            # 文件写入
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(response_blog)
            print(title)
