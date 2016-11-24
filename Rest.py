import requests

class rest:
    def __init__(self,headers,url):
        self.headers = headers
        self.url = url
    
    def post(self,msj):
        return requests.post(self.url, data=msj, headers=self.headers).text
