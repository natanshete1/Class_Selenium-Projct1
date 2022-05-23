from Locators.loginLocators import LoginLocators
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_txtbox_name = LoginLocators.email_txtbox_name
        self.pass_txtbox_name = LoginLocators.pass_txtbox_name
        self.login_btn_name = LoginLocators.login_btn_name

    def enter_email(self, email):
        self.driver.find_element(By.XPATH,self.email_txtbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.pass_txtbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_btn_name).click()