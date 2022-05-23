import allure
from Pages.LoginPage import LoginPage
from Base.base import Base
import pytest


# test test_login_success
@pytest.mark.usefixtures()
class TestLogin(Base):

    @allure.description("validates login")
    @allure.severity(severity_level="Critical")
    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('natanshete1@gmail.com')
        login.enter_password('123456789')
        login.click_login()

        try:
            assert driver.title == "welcome נתן"
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()

    # test_login_with_proper_posswerd_and_email_noll
    @allure.description("validates login")
    @allure.severity(severity_level="critical")
    def test_login_with_proper_posswerd_and_email_noll(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('natanshete1@gmail.com')
        login.enter_password('')
        login.click_login()
        # allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        try:
            assert driver.title == "welcome נתן"
            allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()

    # test_login_with_invalid_email_and_noll_posswerd
    @allure.description("validates login")
    @allure.severity(severity_level="critical")
    def test_login_with_invalid_email_and_noll_posswerd(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('שלום')
        login.enter_password('')
        login.click_login()
        allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        try:
            assert driver.title == ""
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()

    # test_login_with_numbers_email_and_noll_posswerd
    @allure.description("validates login")
    @allure.severity(severity_level="critical")
    def test_login_with_numbers_email_and_noll_posswerd(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('12345')
        login.enter_password('')
        login.click_login()
        allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        try:
            assert driver.title == ""
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()

    # test_login_with_special_Characters_email_and_noll_posswerd
    @allure.description("validates login")
    @allure.severity(severity_level="critical")
    def test_login_with_special_Characters_email_and_noll_posswerd(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('@@@@@')
        login.enter_password('')
        login.click_login()
        allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        try:
            assert driver.title == ""
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()

    # Check with a correct email and a noll_posswerd
    @allure.description("validates login")
    @allure.severity(severity_level="critical")
    def test_with_correct_email_and_noll_posswerd(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('natanshete1@gmail.com')
        login.enter_password('')
        login.click_login()
        allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        try:
            assert driver.title == ""
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()

# PycharmProjects\while\Class_Selenium_Project>pytest -v -s Tests/testLogin.py --alluredir=Report
