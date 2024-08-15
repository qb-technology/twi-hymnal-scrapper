from utilities.driver import WebDriver
from pprint import pprint


class Scrapper(WebDriver):
    # always accept main pages url
    def __init__(self):
        super().__init__()

    def start(self, url, type_):
        # open chrome driver
        self.setup(url, type_)
        # readLinks
        self.readLinks()
        if (len(self.links[:1]) > 0):
            for link in self.links:
                self.readPage(link)

        self.writeJSON(self.json_data)
        print(f'Number of links: {len(self.links)
                                  }\nNumber of saved data {len(self.json_data)}')
        self.reset()
        return


if (__name__ == '__main__'):
    inputs = [
        ("https://www.hymnalaccompanist.com/twi/twinumber.html", "num"),
        ("https://www.hymnalaccompanist.com/twi/n-title.html", "n"),
        ("https://www.hymnalaccompanist.com/twi/ng-title.html", "ng")
    ]
    scrap = Scrapper()
    for inp in inputs:
        scrap.start(inp[0], inp[1])

    scrap.stop()
