# Name:github_spider
# Author:Yasu
# Time:2020/3/14

from lxml import etree
import requests



class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/'
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/80.0.3987.132 Safari/537.36'
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div/input[1]/@value')[0]
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath()