from lxml import etree
import requests


test_url = "http://blog.sina.com.cn/twocold"
resp = requests.get(test_url).content
print(resp.decode('utf-8'))
html = etree.HTML(resp)

#titles = html.xpath('//*[@class="blog_title"]/a/text()')
titles = html.xpath('//*[@class="tag SG_txtc"]/text()[1]')
#titles = html.xpath('//*[@id="t_10001_4701280b0102wruo"]/a/text()')
print(titles)