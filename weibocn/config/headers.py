import random


class FakeChromUA:
    first_num = random.randint(32, 76)
    second_num = random.randint(3200, 3809)
    third_num = random.randint(100, 132)
    chrome_version = "Chrome/{}.0.{}.{}".format(first_num, second_num, third_num)
    os_type = random.choice(['(Windows NT 10.0; Win64; x64)', '(Windows NT 6.1; WOW64)', '(Macintosh; Intel Mac OS X 10_12_6)'])

    @classmethod
    def get_ua(cls):
        return "Mozilla/5.0 {} AppleWebKit/537.36 (KHTML, like Gecko) {} Safari/537.36".format(cls.os_type, cls.chrome_version)


headers = {
    "Connection": "keep-alive",
    "User-Agent": FakeChromUA.get_ua(),
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7"
}
