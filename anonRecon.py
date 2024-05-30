import mechanize
import time
import random
import http.cookiejar as cookielib  # Updated import for Python 3

class anonRecon(mechanize.Browser):
    def __init__(self, proxies=[], user_agent=[]):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies = proxies
        self.user_agents = user_agent + ['Mozilla/4.0', 'FireFox/6.01', 'Nokia7110/1.0']
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
        self.anonymize()

    def clear_cookies(self):
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)

    def change_user_agent(self):
        index = random.randrange(0, len(self.user_agents))
        self.addheaders = [('User-agent', self.user_agents[index])]

    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies({'http': self.proxies[index]})

    def anonymize(self, sleep=False):
        self.clear_cookies()
        self.change_user_agent()
        self.change_proxy()
        if sleep:
            time.sleep(60)

ab = anonRecon(proxies=[], user_agent=['anonBrowser'])
for attempt in range(1, 5):
    ab.anonymize()
    print('[*] Fetching Page')
    response = ab.open('https://google.com')
    for cookie in ab.cookie_jar:
        print(cookie)
