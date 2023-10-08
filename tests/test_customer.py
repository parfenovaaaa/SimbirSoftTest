import allure

from step.customers_steps import CustomersSteps
from utils.common_utils import get_amount, TransactionType, Customers
import pytest_check as check


class TestCustomer:
    @allure.feature("Customers tests")
    @allure.story("Check customers transactions")
    def test_customer_debit_credit(self, customer_steps: CustomersSteps, attach_csv_teardown):
        """
        Make deposit and withdrawl transaction on same amount and check balance
        """
        amount = get_amount()
        transactions_count = 2
        customer_steps.login_as_customer(Customers.HarryPotter)
        start_balance = customer_steps.customer_page.get_customer_balance()
        check.equal(start_balance, 0)
        customer_steps.check_transaction(amount=amount, transaction_type=TransactionType.deposit)
        customer_steps.check_transaction(amount=amount, transaction_type=TransactionType.withdrawl)
        end_balance = customer_steps.customer_page.get_customer_balance()
        check.equal(start_balance, end_balance)
        attach_csv_teardown(customer_steps.transactions_page.get_customer_transactions(transactions_count))
