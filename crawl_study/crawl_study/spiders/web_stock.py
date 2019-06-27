import requests


query_url = "https://trade.gtja.com/webtrade/trade/fundsAction.do?method=searchAllFunds"
#query_url = "https://trade.gtja.com/webtrade/trade/webTradeAction.do?method=getHq&stkcode=000651&bsflag=B"
test_header = {
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)",
    "Referer":"https://trade.gtja.com/webtrade/trade/menu.jsp?menu=stock&elecps=null"
    #"Referer":"https://trade.gtja.com/webtrade/trade/PaperBuy.jsp"
}

test_cookies = {
    "JSESSIONID":"D2njcvpL4QQ2vzWHZ5RNlKK224zCJj0pZCGHvGjXvzKJJg2BbfPk!1235977884"
}

r = requests.get(query_url,headers = test_header, cookies = test_cookies)
print(r.status_code)
print(r.content)