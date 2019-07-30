import random


first_num = random.randint(55,75)
third_num = random.randint(0,3770)
fourth_num = random.randint(0,142)


class FakeChromeUA:
    os_type = [
        '(Windows NT 10.0; Win64; x64)',
        '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = "Chrome/{}.0.{}.{}".format(first_num, third_num, fourth_num)

    @classmethod
    def get_ua(cls):
        return 'Mozilla/5.0 {} AppleWebKit/537.36 (KHTML, like Gecko) {} Safari/537.36'.format(random.choice(cls.os_type), cls.chrome_version)


headers = {
    'User-Agent': FakeChromeUA.get_ua()
}




