import requests

USER="admin"
PASS="admin"
SERVER_IP="192.168.1.10"


class Client(object):
    cookie = ""
    stream_url = ""
    def __init__(self, user, password, ip):
        assert user and password and ip, "Missing params"
        self.user = user
        self.password = password
        self.ip = ip

    def login(self):
        url="http://{IP}/Login.cgi?Username={USER}&Password={PASSWORD}".format(IP=self.ip,USER=self.user,PASSWORD=self.password)
        resp = requests.get(url)
        data = resp.text.split(';')
        params = {}
        for i in data:
            try:
                k,v = i.split("=")
                params[k] = v
            except:
                pass
        self.cookie  = params.get('Session-ID')
        self.stream_url ="http://{IP}/Getvideo.cgi?Cookie={COOKIE}".format(IP=self.ip,COOKIE=self.cookie)
        return params
