from page_prase import prase_by_privince, prase_by_city

url = "https://price.ccement.com"
if __name__ == '__main__':
    url = "https://price.ccement.com"
    city_url = "https://price.ccement.com/pricenewslist-1-440000-440400.html"
    province_url = "https://price.ccement.com/pricenewslist-1-610000-0.html"
    price_url = "https://price.ccement.com/news/202008261713531002.html"
    #prase_by_privince(url)
    #prase_by_date(city_url)
    prase_by_city(province_url)
    #prase_by_page(price_url)