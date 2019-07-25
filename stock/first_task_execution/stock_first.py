from db import dao

stock_info_path = 'stocks.txt'

with open(stock_info_path) as f:
    for line in f.readlines():
        stock_info = line.strip()
