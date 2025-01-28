from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

fav_btn = (By.CLASS_NAME,'FavoritesButton_button__oIuqE')



class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.21vek.by/portable_audio/2yndx00026vio_yandex_9211399.html?recommendationId=ab0424e8d159447f97fb1918a2241d52')
    
    def get_fav_btn(self):
        return self.find(fav_btn)
    
    def click_fav_btn(self):
        self.get_fav_btn().click()

    def get_attribute(self):
        return self.get_fav_btn().get_attribute('aria-label')

   