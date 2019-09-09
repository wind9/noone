import requests


api_url = "http://hq.sinajs.cn/list={}"


def get_stock_info(stocks):
    stock_info_list = []
    if isinstance(stocks, list):
        pass
    stock_codes = []
    for s in stocks:
        if s.startswith('sz') or s.startswith('sh'):
            stock_codes.append(s)
        else:
            stock_codes.append('sh'+ s)
            stock_codes.append('sz'+ s)
    params = ",".join(stock_codes)
    r = requests.get(api_url.format(params))
    resp = r.content.decode('gbk')
    #print(resp)
    for line in resp.split('\n'):
        stock_info = {}
        if not line:
            break
        if not line.endswith('"";'):
            #print(line)
            stock_code = line.split('=')[0].replace('var hq_str_','')
            #print(line.split('=')[1])
            #print(line)
            #print('---------')
            stock_info_body = line.split('=')[1].strip(';').strip('"')
            #print(stock_info_body)
            stock_info['stock_code'] = stock_code
            stock_info['stock_name'] = stock_info_body.split(',')[0]
            stock_info['start_price'] = stock_info_body.split(',')[1]
            stock_info['current_price'] = stock_info_body.split(',')[2]
            stock_info['max_price'] = stock_info_body.split(',')[3]
            stock_info['current_time'] = stock_info_body.split(',')[-2]
            stock_info_list.append(stock_info)
    return stock_info_list



if __name__ == '__main__':
    query_stocks = ['150223','150224','sz150153','150152']
    result = get_stock_info(query_stocks)
    merge_cy_price = 0
    merge_zq_price = 0
    for r in result:
        print(r)
        stock_name = r['stock_name']
        if "证券" in stock_name:
            merge_zq_price = merge_zq_price + float(r['current_price'])
        if "创业" in stock_name:
            merge_cy_price = merge_cy_price + float(r['current_price'])
    print("证券",merge_zq_price*553)
    print("创业",merge_cy_price*494)