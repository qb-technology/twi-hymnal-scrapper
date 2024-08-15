from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import json


class WebDriver:
    options = Options()
    url = ''
    type = ''  # num, n, ng
    driver = None
    links = []
    json_data = []
    twi_translation_table = str.maketrans('xXqQ', 'ɔƆɛƐ')

    def __init__(self, url, type):
        assert isinstance(url, str)
        assert isinstance(type, str)
        self.url = url
        self.type = type
        self.options.add_argument("start-maximized")
        self.options.add_argument('--headless=new')
        self.options.add_argument('--disable-dev-shm-usage')
        # self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')

    def open(self):
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)

    def stop(self):
        self.driver.quit()

    def readLinks(self):
        if (self.type == 'ng'):
            tr_link = self.driver.find_elements(by=By.TAG_NAME, value='td')
            links = tr_link[-1].find_elements(
                by=By.CSS_SELECTOR, value='a')
            self.links = [link.get_attribute('href') for link in links]
        else:
            links = self.driver.find_elements(
                by=By.CSS_SELECTOR, value='a.hintanchor')
            self.links = [link.get_attribute('href') for link in links]

    def parseTwi(self, txt):
        assert isinstance(txt, str)
        return txt.translate(self.twi_translation_table)

    def readPage(self, url):
        twi = ''
        eng = ''
        title = ''
        print(f'fetching {url}')
        self.driver.get(url)
        print(f'page opened')
        title = self.driver.find_element(by=By.TAG_NAME, value='b').text
        div_contains = self.driver.find_elements(
            by=By.CSS_SELECTOR, value='td>div')
        twi = div_contains[0].text
        twi = self.parseTwi(twi)
        if (len(div_contains) > 1):
            eng = div_contains[1].text
        print(title)
        # print('--------------------------------')
        print(twi)
        # print('--------------------------------')
        print(eng)
        res = {
            'twi': twi,
            'eng': eng,
            'title': title
        }
        self.json_data.append(res)
        return res

    def readJSON(self):
        with open(f'../data/hymn_{self.type}', 'r') as f:
            data = json.load(f)
        return data

    def writeJSON(self, payload):
        # Construct the directory and file path
        directory = '../data/'
        file_path = f'{directory}hymn_{self.type}.json'

        # Create the directory if it does not exist
        os.makedirs(directory, exist_ok=True)

        # Write the JSON data to the file
        with open(file_path, 'w') as f:
            json.dump(payload, f)

    def reset(self):
        self.json_data = []
        self.links = []
        return
