from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


catalogSearch = (By.ID,'catalogSearch')
sortTools = (By.CSS_SELECTOR,'li.cr-tools-sort__bi')
ascIcon = (By.CSS_SELECTOR,'g-cr-asc')
chbox = (By.CSS_SELECTOR,'label[title="Idea"]')
filter_submit = (By.CLASS_NAME,'filter-controls__submit')
result_name = (By.CLASS_NAME,'result__name')


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def get_catalog_search(self):
        return self.find_wait(catalogSearch)
    
    def click_catalog_search(self):
        self.get_catalog_search().click()

    def select_catalog(self,name):
        self.get_catalog_search().send_keys(name)
        self.get_catalog_search().send_keys(Keys.RETURN)

    def get_sortTools(self):
        return self.find_wait(sortTools)
    
    def click_sortTools(self):
        self.get_sortTools().click()

    def get_ascIcon(self):
        return self.find_wait(ascIcon)

    def get_chbox(self):
        return self.find(chbox)
    
    def click_chbox(self):
        self.get_chbox().click()

    def get_filter_submit(self):
        return self.find_wait(filter_submit)
    
    def click_filter_submit(self):
        self.get_filter_submit().click()

    def get_names(self):
        return self.browser.find_elements(result_name)
