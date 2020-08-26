from page_prase.basic import get_selector, get_html
from tasks import app
from logger import log
from db import MarketInfo
import re


def prase_by_privince(url):
    selector = get_selector(url)
    locations = selector.xpath('//div[contains(@class,"cityhot_list")]/p')
    for location in locations:
        province_list = location.xpath('//a[@class="item"]')
        for p in province_list:
            province_url = p.xpath('@href')[0]
            province_name = p.xpath('text()')[0]
            app.send_task('tasks.area.do_city_list', args=(province_url,), queue='area')
            log.info('正在处理{},url:{}'.format(province_name, province_url))


def prase_by_city(url):
    selector = get_selector(url)
    city_list = selector.xpath('//div[contains(@class,"areacon")]/a')
    for city in city_list:
        city_url = city.xpath('@href')[0]
        city_name = city.xpath('text()')[0]
        app.send_task('tasks.area.do_date_list', args=(city_url,), queue='area')
        log.info('正在处理{},url:{}'.format(city_name, city_url))


def prase_by_date(url):
    selector = get_selector(url)
    date_list = selector.xpath('//div[contains(@class,"list_list")]/ul/li/a')
    for d in date_list:
        price_url = d.xpath('@href')[0]
        #price_date = d.xpath('text()')[0]
        price_date = d.getparent().xpath('span/text()')[0].strip('[').strip(']')
        app.send_task('tasks.area.do_page_info', args=(price_url,), queue='area')
        log.info('正在处理{},url:{}'.format(price_date, price_url))


def prase_by_page(url):
    selector = get_selector(url)
    title = selector.xpath('//h1[contains(@class,"p_area_title")]/text()')[0]
    date_info = selector.xpath('//div[contains(@class,"infotxt")]/span/text()')[0]
    price_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', date_info)[0]
    table_list = selector.xpath('//div[contains(@class,"p_area_left")]//tr[contains(@class,"price_table_list")]')
    price_info_list = []
    for line in table_list:
        market_info = MarketInfo()
        market_info.price_date = price_date
        market_info.brand = line.xpath('td[1]/a/text()')[0]
        # price_date = d.xpath('text()')[0]
        market_info.sn_type = line.xpath('td[2]/text()')[0]
        if line.xpath('td[4]/span'):
            market_info.price = line.xpath('td[4]/span/text()')[0]
        else:
            market_info.price = line.xpath('td[4]/text()')[0].strip()
        market_info.company = line.xpath('td[6]/text()')[0]
        price_info_list.append(market_info)
        log.info('正在处理{},日期:{},品牌:{},价格:{}'.format(title, price_date, market_info.brand, market_info.price))
    app.send_task('tasks.db.save_data', args=(title, price_info_list))


if __name__ == '__main__':
    city_url = "https://price.ccement.com/pricenewslist-1-440000-440400.html"
    province_url = "https://price.ccement.com/pricenewslist-1-440000-0.html"
    price_url = "https://price.ccement.com/news/202008261713531002.html"
    #prase_by_date(city_url)
    #prase_by_city(province_url)
    prase_by_page(price_url)