from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



cookie_btn1 = (By.CLASS_NAME,'AgreementCookie_reject__f5oqP')
cookie_btn2 = (By.CLASS_NAME,'Button-module__gray-secondary')
userToolsToggler = (By.CLASS_NAME,'styles_userToolsToggler__c2aHe')
userToolsBtn = (By.CLASS_NAME,'userToolsBtn')
login_email = (By.ID,'login-email')
login_password = (By.ID,'login-password')
login_submit = (By.CSS_SELECTOR,"button[data-testid='loginSubmit']")
modal_close = (By.CSS_SELECTOR,"button[data-testid='modalClose']")
userToolsSubtitle = (By.CLASS_NAME,'userToolsSubtitle')

class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.21vek.by/')
    
    def close_cookie_agrement(self):
        self.find_wait(cookie_btn1).click()
        self.find(cookie_btn2).click()

    def get_ToolsToggler(self):
        return self.find(userToolsToggler)
    
    def click_ToolsToggler(self):
        self.get_ToolsToggler().click()

    def get_userToolsBtn(self):
        return self.find(userToolsBtn)
    
    def click_userToolsBtn(self):
        self.get_userToolsBtn().click()

    def get_login_email(self):
        return self.find(login_email)
    
    def enter_email(self,mail):
        self.get_login_email().send_keys(mail)

    def get_login_password(self):
        return self.find(login_password)
    
    def enter_login_password(self,password):
        self.get_login_password().send_keys(password)

    def get_login_submit(self):
        return self.find_wait(login_submit)
    
    def click_login_submit(self):
        self.get_login_submit().click()

    def get_modal_close(self):
        return self.find_wait(modal_close)
    
    def click_modal_close(self):
        self.get_modal_close().click()

    def get_subtitle(self):
        return self.find(userToolsSubtitle)
    
    def get_user_mail(self):
        return self.get_subtitle().text
