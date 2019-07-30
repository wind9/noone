import requests
from config import headers
from config import get_urls, get_cookies
from utils import parse_time
from db.dao import StockDayPriceOper
import json
from logger import storage
from tasks import app


def get_stock_info(stock_code, start_date, end_date):
    urls = get_urls()
    xq_url = urls.get('xueqiu')
    xq_headers = headers
    xq_cookies = get_cookies()['xueqiu']
    start_timestamp = parse_time.date2timstamp(start_date)
    end_timestamp = parse_time.date2timstamp(end_date)
    now_timestamp = parse_time.get_now_timestamp()
    period = "1day"
    price_type = 'before'
    req_url = xq_url.format(stock_code, period, price_type, start_timestamp, end_timestamp, now_timestamp)
    resp = requests.get(req_url, headers=headers, cookies = xq_cookies)
    jdata = json.loads(resp.content)
    return jdata

def get_stock_info2(stock_code):
    urls = get_urls()
    xq_url = urls.get('xueqiu2')
    xq_headers = headers
    xq_cookies = get_cookies()['xueqiu']
    period = "1day"
    price_type = 'before'
    req_url = xq_url.format(stock_code, period, price_type)
    day_price_list = []
    try:
        resp = requests.get(req_url, headers=headers, cookies = xq_cookies)
        price_info = json.loads(resp.content)
        if price_info['success'] == 'true':
            for d in price_info['chartlist']:
                stock_day_price = {}
                stock_day_price['trade_date'] = parse_time.timestamp2date(d['timestamp']/1000)
                stock_day_price['stock_code'] = stock_code
                stock_day_price['open'] = d['open']
                stock_day_price['close'] = d['close']
                stock_day_price['high'] = d['high']
                stock_day_price['low'] = d['low']
                stock_day_price['chg'] = d['chg']
                stock_day_price['percent'] = d['percent']
                stock_day_price['volume'] = d['volume']
                stock_day_price['lot_volume'] = d['lot_volume']
                day_price_list.append(stock_day_price)
                #result = '{}\t{}\t{}\t{}\t{}\t{}'.format(time, open, close, high, low, percent)
    except Exception as e:
        print(e)
        storage.log("获取{}信息异常".format(stock_code))
        storage.exception(e)
    finally:
        return day_price_list


@app.task
def save_day_price(stock_price_info):
    stock_code = stock_price_info['stock_code']
    trade_date = stock_price_info['trade_date']
    open = stock_price_info['open']
    high = stock_price_info['high']
    close = stock_price_info['close']
    low = stock_price_info['low']
    chg = stock_price_info['chg']
    percent = stock_price_info['percent']
    volume = stock_price_info['volume']
    lot_volume = stock_price_info['lot_volume']
    StockDayPriceOper.insert_day_price(stock_code, trade_date, open, high, close, low, chg, percent, volume, lot_volume)


if __name__ == '__main__':
    stock_code = 'SZ000651'
    for price_info in get_stock_info2(stock_code):
        print(price_info)


