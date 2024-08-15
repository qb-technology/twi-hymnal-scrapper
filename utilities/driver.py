from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class WebDriver:

    def __init__(self, url):
        assert isinstance(url, str)
        self.url = url
        self.links = []
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_argument('--headless=new')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.chrome(self.options)
        self.driver.get(url)

    def stop(self):
        self.driver.quit()

    def readLinks(self):
        links = self.driver.find_elements(
            by=By.CSS_SELECTOR, value='a.hintanchor')
        self.links = [link.get_attribute('href') for link in links]

    def readPage(self, url):
        pass
