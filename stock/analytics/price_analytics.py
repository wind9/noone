from db.dao import StockDayPriceOper
import matplotlib.pyplot as plt

gl_code = 'SZ000651'
md_code = 'SZ000333'
start_date = '2016-08-01'
end_date = '2019-08-01'


def get_price(stock_code, start_date, end_date):
    price_info = {}
    stocks = StockDayPriceOper.get_day_price(stock_code, start_date, end_date)
    for stock in stocks:
        trade_date = stock.trade_date
        open = stock.open
        price_info[trade_date] = open
    return price_info


def sorted_kv(item):
    klist = []
    vlist = []
    for k in sorted(item.keys()):
        klist.append(k)
        vlist.append(item[k])
    return klist,vlist


gl = get_price(gl_code, start_date, end_date)
md = get_price(md_code, start_date, end_date)
gl_x, gl_y = sorted_kv(gl)
md_x, md_y = sorted_kv(gl)
common_x = []
common_y = []
common = {}
for k in gl.keys():
    if k in md:
        common_x.append(k)
        bizhi = gl[k]/md[k]
        common_y.append(bizhi)
        common[k] = bizhi
# plt.scatter(common_x, common_y, alpha=0.6)
# #plt.plot(common_x, common_y, color = 'r')
# plt.savefig('gl.png', dpi=1920)
# plt.show()
i = 0
common_y.sort()
print(common)
for bizhi in common_y:
    i = i +1
    print(i, bizhi)
