import requests
import lxml.etree as le
import re

url = 'https://so.csdn.net/so/search/s.do?p={page}&q={keyword}&t=blog&viparticle=&domain=&o=&s=&u=&l=&f=&rbg=0'


def getResponse(url):
    req = requests.get(
        url=url,
        allow_redirects=False,
        headers={
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            'User-Agent': 'mozilla/5.0 (Windows nt 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            # "connnction": "keep-alive",
        }
    )
    response = req.content.decode('utf-8','ignore')
    return response


if __name__ == '__main__':
    # keyword = input('关键词')
    # pn_start = int(input('起始页'))
    # pn_end = int(input('终止页'))


    keyword = 'python-debug'
    pn_start = 1
    pn_end = 1

    for page in range(pn_start, pn_end + 1):
        # 访问1级页面
        response = getResponse(
            url='https://so.csdn.net/so/search/all?q={keyword}&t=all&p={page}&s=0&tm=0&lv=-1&ft=0&l=&u='.format(
                page=page, keyword=keyword)
        )
        print(response)
        # 二级页面，博客的链接
        hrefs = le.HTML(response).xpath('//div[@class="search-list-con"]/dl//span[@class="mr16"]/../../dt/div/a[1]/@href')
        print(hrefs)
        for href in hrefs:
            response_blog = getResponse(
                url = href,
            )
            title = le.HTML(response_blog).xpath('//h1[@class="title-article"]/text()')[0]
            title = re.sub(
                r'[/\\:*"<>|?]','',title
            )
            filepath = 'blog/%s.html' % title
            with open(filepath,'wb') as f:
                f.write(response_blog)

            print(title)

