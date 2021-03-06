from page_prase.basic import get_selector
from tasks import app
from logger import log
from db import MarketInfo, CommonOper
import re


def prase_by_privince(url):
    selector = get_selector(url)
    if selector:
        locations = selector.xpath('//div[contains(@class,"cityhot_list")]/p')
        for location in locations:
            province_list = location.xpath('//a[@class="item"]')
            for p in province_list:
                province_url = p.xpath('@href')[0]
                province_name = p.xpath('text()')[0]
                app.send_task('tasks.area.do_city_list', args=(province_url,), queue='area')
                log.info('正在处理省份:{},url:{}'.format(province_name, province_url))


def prase_by_city(url):
    selector = get_selector(url)
    if selector:
        city_list = selector.xpath('//div[contains(@class,"areacon")]/a')
        for city in city_list:
            city_url = city.xpath('@href')[0]
            city_name = city.xpath('text()')[0]
            app.send_task('tasks.area.do_date_list', args=(city_url,), queue='area')
            log.info('正在处理城市:{},url:{}'.format(city_name, city_url))


def prase_by_date(url):
    selector = get_selector(url)
    if selector:
        date_list = selector.xpath('//div[contains(@class,"list_list")]/ul/li/a')
        for d in date_list:
            price_url = d.xpath('@href')[0]
            price_date = d.getparent().xpath('span/text()')[0].strip('[').strip(']')
            app.send_task('tasks.area.do_page_info', args=(price_url,), queue='area')
            #log.info('正在处理{},url:{}'.format(price_date, price_url))
        next_page_url = selector.xpath('//a[@class="next_page"][contains(text(),"下一页")]/@href')
        if next_page_url:
            log.info("当前页:{},处理下一页:{}".format(url, next_page_url[0]))
            app.send_task('tasks.area.do_date_list', args=(next_page_url[0],), queue='area')


def prase_by_page(url):
    selector = get_selector(url)
    if selector:
        title = selector.xpath('//h1[contains(@class,"p_area_title")]/text()')[0]
        province = selector.xpath('/html/body/div[6]/div[1]/ul/li[4]/a/text()')[0].strip('省')
        pattern = re.compile(province+'(.*)水泥')
        city = re.findall(pattern, title)[0]
        date_info = selector.xpath('//div[contains(@class,"infotxt")]/span/text()')[0]
        price_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', date_info)[0]
        table_list = selector.xpath('//div[contains(@class,"p_area_left")]//tr[contains(@class,"price_table_list")]')
        price_info_list = []
        for line in table_list:
            market_info = MarketInfo()
            market_info.province = province
            market_info.city = city
            market_info.price_date = price_date
            market_info.brand = line.xpath('td[1]/a/text()')[0]
            # price_date = d.xpath('text()')[0]
            market_info.sn_type = line.xpath('td[2]/text()')[0]
            if line.xpath('td[4]/span'):
                market_info.price_desc = line.xpath('td[4]/span/text()')[0]
            else:
                market_info.price_desc = line.xpath('td[4]/text()')[0].strip()
            price_pattern = '(\d{3})'
            price_section = re.findall(price_pattern, market_info.price_desc)
            if price_section:
                market_info.price = (float(price_section[0]) + float(price_section[1]))/2
            else:
                market_info.price = 0
            market_info.company = line.xpath('td[6]/text()')[0]
            price_info_list.append(market_info)
            #CommonOper.add_one(market_info)
            #log.info('正在处理{},日期:{},品牌:{},价格:{}'.format(title, price_date, market_info.brand, market_info.price))
        log.info('正在处理{}'.format(title))
        CommonOper.add_all(price_info_list)
        #app.send_task('tasks.db.save_data', args=(title, json.dumps(price_info_list),), queue='area')


if __name__ == '__main__':
    city_url = "https://price.ccement.com/pricenewslist-1-440000-440400.html"
    city_url = "https://price.ccement.com/pricenewslist-34-440000-440400.html"
    province_url = "https://price.ccement.com/pricenewslist-1-440000-0.html"
    price_url = "https://price.ccement.com/news/202008261713531002.html"
    #prase_by_date(city_url)
    #prase_by_city(province_url)
    prase_by_page(price_url)