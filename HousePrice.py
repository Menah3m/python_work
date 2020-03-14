
import requests
from lxml import etree


def getprice():
    start_url = 'https://cd.newhouse.fang.com/house/s/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
    res = requests.get(start_url, headers=headers)
    ret = res.content.decode('gbk')  # ret为当前网页源代码
    # print(ret)
    result = etree.HTML(ret)  # 要使用XPath提取数据的话，必须先转换成XML数据
    content_list = result.xpath('//div[@id="newhouse_loupai_list"]/ul/li')
    for content in content_list:
        title = content.xpath('.//div[@class="nlcd_name"]/a/text()')
        title = title[0].strip() if len(title) > 0 else ''
        print(title)


#TODO 完成代码重构


if __name__ == '__main__':
    getprice()
