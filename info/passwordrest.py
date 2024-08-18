import requests
from termcolor import cprint

class passwordres:

    def __init__(self,url):

        self.url = url

    def checkpass(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate"
        }
        payload = 'member/reg_new.php'

        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)

            if "系统关闭了会员功能" in r.text:
                return
            else:
                cprint("可能存在dede任意用户重置漏洞:https://www.t00ls.net/thread-43689-1-1.html","red")
        except:
            return False
