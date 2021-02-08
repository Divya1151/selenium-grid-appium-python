from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from pages.locator import Locator
import time

class Login(object):
    def __init__(self, driver):
        self.driver = driver 
        
    def login_into_app(self):
        self.auth_login = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.ID, Locator.auth_login))
        self.auth_login.click()
        self.auth_login2 = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.ID, Locator.auth_login2))
        self.auth_login2.click()
        self.email_button = WebDriverWait(self.driver, 20).until(lambda x: x.find_element(MobileBy.ID, Locator.email_button))
        self.email_button.click()
        self.username = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(MobileBy.ID, Locator.email))
        self.username.send_keys("ankit@ankitkumar.dev")
        self.button_next = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(MobileBy.ID, Locator.button_next))
        self.button_next.click()
        self.password = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(MobileBy.ID, Locator.password))
        self.password.send_keys("Ankit1234")
        self.signin = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(MobileBy.ID, Locator.signin))
        self.signin.click()
        time.sleep(2)
        
    