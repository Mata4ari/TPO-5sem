from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
from pages.MainPage import MainPage

class VekTests(unittest.TestCase):
    def setUp(self):
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(options=chrome_options)
            mainPage = MainPage(self.driver)
            mainPage.open()
            mainPage.close_cookie_agrement()