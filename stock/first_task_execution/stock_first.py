from db import dao
from db.models import StockInfo
from db.dao import StockInfoOper

stock_info_path = 'stocks.txt'

with open(stock_info_path, encoding="utf-8") as f:
    for line in f.readlines():
        stock_info = line.strip().split("|")
        coop_code = stock_info[0].strip()
        coop_name = stock_info[1].strip()
        stock_code = stock_info[2].strip()
        stock_name = stock_info[3].strip()
        reg_date = stock_info[4].strip()
        total_share = int(stock_info[5].strip().replace(",",""))
        circulating_share = int(stock_info[6].strip().replace(",",""))
        industry = stock_info[7].strip()
        security_type = stock_info[8].strip()
        market = stock_info[9].strip()
        print(stock_name,stock_code)
        StockInfoOper.insert_stock_info(coop_code, coop_name, stock_code, stock_name, reg_date, total_share,
                                        circulating_share, industry, security_type, market)





