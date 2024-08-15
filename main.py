from utilities.driver import WebDriver
from pprint import pprint


class Scrapper(WebDriver):
    # always accept main pages url
    def __init__(self, url, type):
        super().__init__(url, type)

    def start(self):
        # open chrome driver
        self.open()
        # readLinks
        self.readLinks()
        print(f'Number of links: {len(self.links)}')
        if (len(self.links) > 0):
            for link in self.links[:1]:
                self.readPage(link)

        self.writeJSON(self.json_data)
        self.reset()
        self.stop()


if (__name__ == '__main__'):
    m_url = "https://www.hymnalaccompanist.com/twi/twinumber.html"
    n_url = "https://www.hymnalaccompanist.com/twi/n-title.html"
    ng_url = "https://www.hymnalaccompanist.com/twi/ng-title.html"
    scrap = Scrapper(m_url, 'num')
    # scrap = Scrapper(n_url, 'n')
    # scrap = Scrapper(ng, 'ng')
    scrap.start()
