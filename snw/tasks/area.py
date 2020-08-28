from tasks import app
from page_prase import prase_by_privince, prase_by_city, prase_by_date, prase_by_page
from page_prase.basic import base_url
from db import CommonOper


@app.task()
def do_province_list(url):
    url = base_url + url
    if not CommonOper.isExist('snw', url):
        CommonOper.add_filter_key('snw', url)
        prase_by_privince(url)


@app.task()
def do_city_list(url):
    url = base_url + url
    if not CommonOper.isExist('snw', url):
        CommonOper.add_filter_key('snw', url)
        prase_by_city(url)


@app.task()
def do_date_list(url):
    url = base_url + url
    if not CommonOper.isExist('snw', url):
        CommonOper.add_filter_key('snw', url)
        prase_by_date(url)


@app.task()
def do_page_info(url):
    url = base_url + url
    if not CommonOper.isExist('snw', url):
        CommonOper.add_filter_key('snw', url)
        prase_by_page(url)
