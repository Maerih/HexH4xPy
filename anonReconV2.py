import mechanize
import time
import random
import http.cookiejar as cookielib  

class anonRecon(mechanize.Browser):
    def __init__(self, proxies=[], user_agents=[]):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies = proxies
        self.user_agents = user_agents + ['Mozilla/4.0', 'FireFox/6.01', 'Nokia7110/1.0']
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

    def fetch_page(self, url):
        try:
            response = self.open(url)
            return response
        except Exception as e:
            print(f'Error fetching page: {e}')
            return None

    def print_cookies(self):
        print("Cookies:")
        for cookie in self.cookie_jar:
            print(f'  {cookie.name} = {cookie.value}')

    def print_headers(self, response):
        print("Headers:")
        for header in response.info().items():
            print(f'  {header[0]}: {header[1]}')

    def print_source(self, response):
        print("Source Code:")
        print(response.read().decode('utf-8'))

ab = anonRecon(proxies=[], user_agents=['anonBrowser'])
for attempt in range(1, 5):
    ab.anonymize()
    print('[*] Fetching Page')
    response = ab.fetch_page('http://kittenwar.com')
    if response:
        ab.print_cookies()
        ab.print_headers(response)
        ab.print_source(response)
