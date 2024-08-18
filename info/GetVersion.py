import requests
from termcolor import cprint
import re


class GetVersion:

    def __init__(self,url):
        self.url = url



    def version(self):

        def cheakver(arg):
            ver_histroy = {'20080307': 'v3 or v4 or v5',
                           '20080324': 'v5 above',
                           '20080807': '5.1 or 5.2',
                           '20081009': 'v5.1sp',
                           '20081218': '5.1sp',
                           '20090810': '5.5',
                           '20090912': '5.5',
                           '20100803': '5.6',
                           '20101021': '5.3',
                           '20111111': 'v5.7 or v5.6 or v5.5',
                           '20111205': '5.7.18',
                           '20111209': '5.6',
                           '20120430': '5.7SP or 5.7 or 5.6',
                           '20120621': '5.7SP1 or 5.7 or 5.6',
                           '20120709': '5.6',
                           '20121030': '5.7SP1 or 5.7',
                           '20121107': '5.7',
                           '20130608': 'V5.6-Final',
                           '20130922': 'V5.7SP1',
                           '20140225': 'V5.6SP1',
                           '20140725': 'V5.7SP1',
                           '20150618': '5.7',
                           '20180109': 'V5.7SP2'
                           }
            ver_list = sorted(list(ver_histroy.keys()))#将键变成列表，并排序
            ver_list.append(arg)#将参数加到末尾
            sorted_ver_list = sorted(ver_list)#重新排序
            return ver_histroy[ver_list[sorted_ver_list.index(arg) ]]#判断是否在其中，并返回其值

        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
            "Content-Type":"application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate"
        }
        payload = "/data/admin/ver.txt"
        if '://' not in self.url:
            self.url = 'http://' + self.url + '/'
        url = self.url
        vulnurl = url + payload
        try:
            r = requests.get(url=vulnurl,headers=headers)
            if r.status_code == 200:
                m = re.search("^(\d+)$", r.text)
                if m:
                    version = cheakver(m.group(1))
                    msg = "探测到dedecms版本:{} version:{}".format(r.text, version)
                    cprint(msg, "red")
        except:
            return False








