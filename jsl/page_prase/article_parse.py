import requests
from lxml import etree
from db.models import Article, Comment, Praise
from db.dao import CommonOper
import datetime

test_url = "https://www.jisilu.cn/question/333142"
answer_url = "https://www.jisilu.cn/question/ajax/get_answer_comments/answer_id-2445201"


def get_article_and_praise(selector):
    article = Article()
    # article_id = selector.xpath('//div[@id="question_topic_editor"]/@data-id')[0]
    # print(article_id)
    article.article_id = selector.xpath('//div[@id="question_topic_editor"]/@data-id')[0]
    article.title = selector.xpath('//div[@class="aw-mod-head"]/h1/text()')[0]
    # poster = selector.xpath('//dd[@class="pull-left"]/a/@data-id')[0]
    # print(poster)
    article.poster = selector.xpath('//dd[@class="pull-left"]/a/@data-id')[0]
    post_time_str = selector.xpath('//div[@class="aw-question-detail-meta"]/div[1]/span[1]/text()')[0].replace("发表时间 ", "")
    article.post_time = datetime.datetime.strptime(post_time_str, "%Y-%m-%d %H:%M")
    access_time_str = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[1]/span/text()')[0]
    article.access_time = datetime.datetime.strptime(access_time_str, "%Y-%m-%d %H:%M")
    praise_list = selector.xpath('//div[@class="aw-question-detail-meta"]/p[contains(@class,"aw-agree-by")]/a/@data-id')
    article.read_num = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[2]/span/text()')[0]
    article.follow_num = selector.xpath('//div[@class="aw-side-bar-mod-body"]/ul/li[3]/span/text()')[0]
    content = selector.xpath('//div[contains(@class,"aw-question-detail-txt")]/text()')
    article.content = "".join(selector.xpath('//div[contains(@class,"aw-question-detail-txt")]/text()'))
    print(article)
    CommonOper.add_one(article)

    #print(len(post_time_str))
    print(post_time_str)
    print(praise_list)


def get_comments_and_praise(selector):
    pass


def parse(url):
    html = requests.get(test_url).content
    selector = etree.HTML(html)
    get_article_and_praise(selector)
    # article, praise1 = get_article_and_praise(selector)
    # comments, praise2 = get_comments_and_praise(selector)
    # answer_list = selector.xpath('//div[@class="aw-item"]')
    # for answer in answer_list:
    #     comment_id = answer.xpath('@id')[0].split('_')[2]
    #     poster = answer.xpath('a/@data-id')[0]
    #     praise_list = answer.xpath('div/div/div[1]/p[2]/a')
    #     for praise in praise_list:
    #         if praise.xpath('@data-id'):
    #             print("\t回复点赞",praise)
    #     print(poster)

parse(test_url)

