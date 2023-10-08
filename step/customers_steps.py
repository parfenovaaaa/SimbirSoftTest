from time import sleep

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from utils.common_utils import TransactionType, Customers
from page.customer_page import CustomerPage
from page.login_page import LoginPage
from page.transactions_page import TransactionsPage
import pytest_check as check


class CustomersSteps:
    
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.customer_page = CustomerPage(driver)
        self.login_page = LoginPage(driver)
        self.transactions_page = TransactionsPage(driver)

    def login_as_customer(self, customer_name: str = Customers.HarryPotter) -> None:
        """
        Log in as customer and check it
        """
        with allure.step(f"Login as customer {customer_name}"):
            self.login_page.login_as_customer(customer_name)
            self.customer_page.check_login_as_customer(customer_name)

    def check_transaction(self, amount: int, transaction_type: str) -> None:
        """
        Make transaction and check it
        """
        with allure.step(f"Make {transaction_type} transaction with amount {amount}"):
            balance_before = self.customer_page.get_customer_balance()
            self.customer_page.make_transaction(amount=amount, transaction_type=transaction_type)
            sleep(1)
            balance_after = self.customer_page.get_customer_balance()
            expected = balance_before + amount if transaction_type == TransactionType.deposit else balance_before - amount
            check.equal(balance_after, expected)
