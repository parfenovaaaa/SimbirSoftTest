from time import sleep

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from page.customer_page import CustomerPage
from page.login_page import LoginPage
from page.transactions_page import TransactionsPage
from utils.common_utils import TransactionType, Customers


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
        wait_transaction = 1
        with allure.step(f"Make {transaction_type} transaction with amount {amount}"):
            balance_before = self.customer_page.get_customer_balance()
            self.customer_page.make_transaction(amount=amount, transaction_type=transaction_type)
            sleep(wait_transaction)
            balance_after = self.customer_page.get_customer_balance()
            expected = balance_before + amount if transaction_type == TransactionType.deposit else balance_before - amount
            assert balance_after == expected, (
                f"Balance changed wrong after {transaction_type}. Expected: {expected}, but got: {balance_after}"
            )
