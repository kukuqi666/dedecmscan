import requests
import json
from urllib.parse import urljoin

class Check:
    def __init__(self, url):
        self.url = url
        self.results = []

    def log_result(self, result):
        self.results.append(result)

    def save_report(self, filename="report.json"):
        with open(filename, "w") as f:
            json.dump(self.results, f, indent=4)
        print(f"[+] Report saved to {filename}")

    def check_http_status(self):
        try:
            response = requests.get(self.url)
            status = {"url": self.url, "status_code": response.status_code}
            if response.status_code == 200:
                status["message"] = "Accessible"
            else:
                status["message"] = f"Returned status code {response.status_code}"
            self.log_result(status)
        except requests.exceptions.RequestException as e:
            self.log_result({"url": self.url, "error": str(e)})

    def detect_sql_injection(self, path):
        payload = "' OR '1'='1"
        try:
            response = requests.get(urljoin(self.url, path), params={'input': payload})
            if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
                print(f"[!] Possible SQL injection vulnerability found at {urljoin(self.url, path)}")
                self.log_result({"url": self.url, "path": path, "vulnerability": "Possible SQL injection"})
            else:
                print(f"[+] No SQL injection vulnerability detected at {urljoin(self.url, path)}")
        except requests.exceptions.RequestException as e:
            self.log_result({"url": self.url, "path": path, "error": str(e)})

    def detect_xss(self, path):
        payload = "<script>alert('XSS')</script>"
        try:
            response = requests.get(urljoin(self.url, path), params={"input": payload})
            if payload in response.text:
                print(f"[!] Possible XSS vulnerability found at {urljoin(self.url, path)}")
                self.log_result({"url": self.url, "path": path, "vulnerability": "Possible XSS"})
            else:
                print(f"[+] No XSS vulnerability detected at {urljoin(self.url, path)}")
        except requests.exceptions.RequestException as e:
            self.log_result({"url": self.url, "path": path, "error": str(e)})

    def detect_rce(self, path):
        payload = "; echo RCE;"
        try:
            response = requests.get(urljoin(self.url, path), params={"input": payload})
            if "RCE" in response.text:
                print(f"[!] Possible RCE vulnerability found at {urljoin(self.url, path)}")
                self.log_result({"url": self.url, "path": path, "vulnerability": "Possible RCE"})
            else:
                print(f"[+] No RCE vulnerability detected at {urljoin(self.url, path)}")
        except requests.exceptions.RequestException as e:
            self.log_result({"url": self.url, "path": path, "error": str(e)})

    def detect_redirect(self, path):
        try:
            response = requests.get(urljoin(self.url, path), allow_redirects=False)
            if 300 <= response.status_code < 400:
                print(f"[!] Possible redirect vulnerability found at {urljoin(self.url, path)}")
                self.log_result({"url": self.url, "path": path, "vulnerability": "Possible Redirect"})
            else:
                print(f"[+] No redirect vulnerability detected at {urljoin(self.url, path)}")
        except requests.exceptions.RequestException as e:
            self.log_result({"url": self.url, "path": path, "error": str(e)})

    def detect_file_inclusion(self, path):
        try:
            response = requests.get(urljoin(self.url, path))
            if "Warning" in response.text or "Error" in response.text:
                print(f"[!] Possible File Inclusion vulnerability found at {urljoin(self.url, path)}")
                self.log_result({"url": self.url, "path": path, "vulnerability": "Possible File Inclusion"})
            else:
                print(f"[+] No File Inclusion vulnerability detected at {urljoin(self.url, path)}")
        except requests.exceptions.RequestException as e:
            self.log_result({"url": self.url, "path": path, "error": str(e)})

    def poc(self):
        print(f"Running PoC on {self.url}")

        # 检查 HTTP 状态码
        self.check_http_status()

        # SQL 注入检测
        sql_paths = [
            "/advancedsearch.php", "/sql_class.php", "/feedback_js.php", "/guestbook.php",
            "/infosearch.php", "/reg_new.php", "/search.php", "/V5order by"
        ]
        for path in sql_paths:
            self.detect_sql_injection(path)

        # XSS 检测
        xss_paths = [
            "/getpage", "/jump.php", "/login.php", "/recommend.php", "/article_keyword_select.php",
            "/catelog_tree.php", "/content_list.php", "/file_pic_vie.php", "/pic_view.php",
            "/select_images.php", "/list.php", "/config.php", "/flash"
        ]
        for path in xss_paths:
            self.detect_xss(path)

        # 文件包含检测
        file_inclusion_paths = [
            "/writebook", "/digg_frame.php"
        ]
        for path in file_inclusion_paths:
            self.detect_file_inclusion(path)

        # 远程代码执行检测
        rce_paths = [
            "/digg_frame.php"
        ]
        for path in rce_paths:
            self.detect_rce(path)

        # 路径检测
        redirect_paths = [
            "/redirect"
        ]
        for path in redirect_paths:
            self.detect_redirect(path)

        # 保存报告
        self.save_report()
