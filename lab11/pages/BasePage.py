from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self,browser):
        self.browser = browser
    
    def find(self,args):
        return self.browser.find_element(*args)
    
    def find_wait(self,arg):
        return WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(arg))
