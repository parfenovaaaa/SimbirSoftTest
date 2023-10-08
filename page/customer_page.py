from time import sleep

import pytest_check as check
from selenium.webdriver.common.by import By

from utils.common_utils import TransactionType, TransactionMessage, Customers
from page.base_page import BasePage


class CustomerPage(BasePage):
    page_url_part = "#/account"
    # Account data
    customer_name = (By.CLASS_NAME, "fontBig")
    account_number_field = (By.CSS_SELECTOR, ".center .ng-binding:nth-child(1)")
    balance_field = (By.CSS_SELECTOR, ".center .ng-binding:nth-child(2)")
    currency_field = (By.CSS_SELECTOR, ".center .ng-binding:nth-child(3)")
    # Account actions
    transactions_btn = (By.CSS_SELECTOR, ".tab:nth-child(1)")
    deposit_btn = (By.CSS_SELECTOR, ".tab:nth-child(2)")
    withdrawl_btn = (By.CSS_SELECTOR, ".tab:nth-child(3)")
    amount_input = (By.CLASS_NAME, "form-control")
    submit_transaction = (By.CLASS_NAME, "btn-default")
    message_field = (By.CLASS_NAME, "error")

    def check_login_as_customer(self, customer_name: str = Customers.HarryPotter) -> None:
        """
        Open customer account page and check its name
        """
        self.open(self.page_url_part)
        text = self.find_element(self.customer_name).text
        assert text == customer_name, f"Error! Logged as {text}, but expected {customer_name}"

    def get_customer_balance(self) -> int:
        """
        Open customer account page and return current balance
        """
        self.open(self.page_url_part)
        return int(self.find_element(self.balance_field).text)

    def make_transaction(self, amount: int, transaction_type: str) -> None:
        """
        Open customer account page and process selected transaction
        """
        self.open(self.page_url_part)
        locator = self.deposit_btn if transaction_type == TransactionType.deposit else self.withdrawl_btn
        self.click_web_element(locator)
        sleep(0.5)
        self.fill_web_element(self.amount_input, amount)
        self.click_web_element(self.submit_transaction)
        message = self.find_element(self.message_field).text
        check.equal(message, TransactionMessage[transaction_type])
