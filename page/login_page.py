import allure
from selenium.webdriver.common.by import By

from common import Customers
from page.base_page import BasePage


# @url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
class LoginPage(BasePage):
    customer_login_btn = (By.XPATH, "//button[@ng-click='customer()']")
    customer_selector = (By.ID, "userSelect")
    login_btn = (By.CLASS_NAME, "btn-default")
    page_url_part = "#/login"

    def login_as_customer(self, customer_name: str) -> None:
        """
        Login as customer by name
        """
        self.open(self.page_url_part)
        self.click_web_element(self.customer_login_btn)
        self.select_web_element_option(self.customer_selector, text=customer_name)
        self.click_web_element(self.login_btn)
