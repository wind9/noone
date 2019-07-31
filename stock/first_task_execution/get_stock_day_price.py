from db.models import StorkDayPrice
from db.dao import StockInfoOper, StockDayPriceOper
from tasks import app, get_stock_info2

stocks = StockInfoOper.get_stock_info()
for stock in stocks:
    stock_code = stock.stock_code
    market = stock.market
    symbol = market + str(stock_code)
    #symbol = 'SH600036'
    day_price_list = get_stock_info2(symbol)
    for stock_price_info in day_price_list:
        app.send_task('tasks.stock.save_day_price',args=(stock_price_info,),queue='store',
                  routing_key='store_route')
    #break
