from lxml import etree
from crawl_study.crawl_study.utils import timeutil
import requests
import os
import hashlib
import threading
import redis
from urllib.parse import urlparse, parse_qs


yzm_url = "http://wapzt.189.cn/wap/getPicRandomCode.do"
test_url = "http://wapzt.189.cn/wap/getPicRandomCode.do?param=1559117050420&sessionid=4765139bfbba460b9caf382921378663&type=2"
redis_client = redis.Redis(host="192.168.88.200", port=6379, password="redis")
redis_client = redis.StrictRedis()
redis_pool = redis.ConnectionPool(host='', port=6379, password="", decode_responses=True)
redis_client = redis.Redis(connection_pool=redis_pool)
url = "https://laoyaoba.com/templates/news/newsdetail?source=pc&news_id=718629"


def get_md5(file_path):
    md5 = None
    if os.path.isfile(file_path):
        with open(file_path , 'rb') as f:
            md5_ojb = hashlib.md5()
            md5_ojb.update(f.read())
            hash_code = md5_ojb.hexdigest()
            md5 = str(hash_code).lower()
    return md5


def download_yzm(timestamp):
    is_repeat = False
    redis_file_path = None
    #timestamp = timeutil.utc13()
    #resp = requests.get(yzm_url + timestamp)
    resp = requests.get(test_url)
    yzm_name = 'I:\\yzm_img\\' + timestamp + '.jpg'
    if resp.status_code == 200:
        with open(yzm_name, 'wb') as f:
            f.write(resp.content)
        md5 = get_md5(yzm_name)
    redis_file_path = redis_client.get(md5)
    if redis_file_path:
        is_repeat = True
        print("当前文件%s与%smd5值相同" % (yzm_name,redis_file_path))
    else:
        redis_client.set(md5, yzm_name)


def run(thread_id):
    for i in range(999):
        timestamp = timeutil.utc13() + str(thread_id) + str(i)
        download_yzm(timestamp)


def test_url(url):
    news_url = url
    params = urlparse(news_url).query
    source = parse_qs(params)['source'][0]
    print(source)


if __name__ == "__main__":
    test_url(url)
    # thread_num = 50
    # thread_list = []
    # for i in range(thread_num):
    #     t = threading.Thread(target = run(i,))
    #     thread_list.append(t)
    # for i in thread_list:
    #     t.setDaemon(True)
    #     t.start()
    # for i in thread_list:
    #     t.join()
