from termcolor import cprint
import threading
from info.GetVersion import GetVersion
from info.FindAdmin import FindAdmin
from info.trace import trace
from info.shortpath import shortpath
from info.passwordrest import passwordres
from info.path import path
from script.advancedsearch_sqli import advancedsearch_sqli
from script.dedesql_class_sqli import dedesql_class_sqli
from script.feedback_js_sqli import feedback_sqli
from script.getpage_xss import getpage_xss
from script.guestbook_sqli import guestbook_sqli
from script.infosearch_sqli import infosearch_sqli
from script.jump_xss import jump_xss
from script.mem_login_xss import jump_xss
from script.recommend_sqli import recomsqli
from script.redirect import redirect
from script.reg_new_sqli import reg_new_sqli
from script.search_sqli import search_sqli
from script.V5orderby import V5orderby
from script.v5xarticlekeywordsselectxss import article_xss
from script.v5xcatalogtreexss import catalogtree_xss
from script.v5xcontentlistxss import content_list_xss
from script.v5xfilepicview import file_pic_vie_xss
from script.v5xpicviewxss import pic_view_xss
from script.v5xselectimages import select_images_xss
from script.v51WriteBookTextgetshell import writebook_getshell
from script.v53diggframerce import dig_frame_rce
from script.v55finalgetshell import final_getshell
from script.v55keywordxss import keyword_xss
from script.v56gourlxss import gourl_xss
from script.v57adminxss import config_xss
from script.v57backdoor import backdoor
from script.v57flashxss import flash_xss



class check:
    def __init__(self,url):

        self.url = url

    def poc(self):

        url = self.url
        cprint("Version checking in progress","magenta")
        dd = GetVersion(url=url)
        t = threading.Thread(target=dd.version())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("find admin in progress","magenta")
        dd = FindAdmin(url=url)
        t = threading.Thread(target=dd.findadmin())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("trace checking in progress","magenta")
        dd = trace(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("shortpath checking in progress","magenta")
        dd = shortpath(url=url)
        t = threading.Thread(target=dd.shortpath())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("password reset checking in progress","magenta")
        dd = passwordres(url=url)
        t = threading.Thread(target=dd.checkpass())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("path checking in progress","magenta")
        dd = path(url=url)
        t = threading.Thread(target=dd.checkpath())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("advancedsearch_sqli checking in progress","magenta")
        dd = advancedsearch_sqli(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("dedesql_class_sqli checking in progress","magenta")
        dd = dedesql_class_sqli(url=url)
        t = threading.Thread(target=dd.checkdedesql())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("feedback_js_sqli checking in progress","magenta")
        dd = feedback_sqli(url=url)
        t = threading.Thread(target=dd.feedcheck())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("getpage_xss checking in progress","magenta")
        dd = getpage_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("guestbook_sqli checking in progress","magenta")
        dd = guestbook_sqli(url=url)
        t = threading.Thread(target=dd.checksql())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("infosearch_sqli checking in progress","magenta")
        dd = infosearch_sqli(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("jump_xss checking in progress","magenta")
        dd = jump_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("recommend_sqli checking in progress","magenta")
        dd = recomsqli(url=url)
        t = threading.Thread(target=dd.checksql())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("redirect checking in progress","magenta")
        dd = redirect(url=url)
        t = threading.Thread(target=dd.check_redirect())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("reg_new_sqli checking in progress","magenta")
        dd = reg_new_sqli(url=url)
        t = threading.Thread(target=dd.checksql())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("search_sqli checking in progress","magenta")
        dd = search_sqli(url=url)
        t = threading.Thread(target=dd.checksqli())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("V5orderby checking in progress","magenta")
        dd = V5orderby(url=url)
        t = threading.Thread(target=dd.checksql())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v5xarticlekeywordsselectxss checking in progress","magenta")
        dd = article_xss(url=url)
        t = threading.Thread(target=dd.checktxss())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v5xcatalogtreexss checking in progress","magenta")
        dd = catalogtree_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v5xcontentlistxss checking in progress","magenta")
        dd = content_list_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v5xfilepicview checking in progress","magenta")
        dd = file_pic_vie_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v5xpicviewxss checking in progress","magenta")
        dd = pic_view_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v5xselectimages checking in progress","magenta")
        dd = select_images_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v51WriteBookTextgetshell checking in progress","magenta")
        dd = writebook_getshell(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v53diggframerce checking in progress","magenta")
        dd = dig_frame_rce(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v55finalgetshell checking in progress","magenta")
        dd = final_getshell(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v55keywordxss checking in progress","magenta")
        dd = keyword_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v56gourlxss checking in progress","magenta")
        dd = gourl_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v57adminxss checking in progress","magenta")
        dd = config_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v57backdoor checking in progress","magenta")
        dd = backdoor(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()
        cprint("v57flashxss checking in progress","magenta")
        dd = flash_xss(url=url)
        t = threading.Thread(target=dd.checktrace())
        t.setDaemon(True)
        t.start()
        t.join()






