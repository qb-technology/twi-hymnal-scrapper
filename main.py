import time
import json

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pprint import pprint

import concurrent.futures

options = Options()
options.add_argument("start-maximized")
options.add_argument('--headless=new')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)


def main():
    driver.get("https://www.hymnalaccompanist.com/twi/twinumber.html")
    links = driver.find_elements(by=By.CSS_SELECTOR, value='a.hintanchor')
    links = [link.get_attribute('href') for link in links]
    pprint(links)
    driver.quit()


if (__name__ == '__main__'):
    m_url = "https://www.hymnalaccompanist.com/twi/twinumber.html"
    n_url = "https://www.hymnalaccompanist.com/twi/n-title.html"
    ng_url = "https://www.hymnalaccompanist.com/twi/ng-title.html"
    main()
