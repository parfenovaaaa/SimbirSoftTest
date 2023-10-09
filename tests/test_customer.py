import allure
import pytest_check

from step.customers_steps import CustomersSteps
from utils.common_utils import get_amount, TransactionType, Customers


class TestCustomer:
    @allure.feature("Customers tests")
    @allure.story("Check customers transactions")
    def test_customer_debit_credit(self, customer_steps: CustomersSteps, attach_csv_teardown):
        """
        Make deposit and withdrawl transaction on same amount and check balance
        """
        amount = get_amount()
        transactions_count = 2
        expected_start_balance = 0
        customer_steps.login_as_customer(Customers.HarryPotter)
        start_balance = customer_steps.customer_page.get_customer_balance()
        pytest_check.equal(start_balance, expected_start_balance, f"Start balance not {expected_start_balance}")
        customer_steps.check_transaction(amount=amount, transaction_type=TransactionType.deposit)
        customer_steps.check_transaction(amount=amount, transaction_type=TransactionType.withdrawl)
        end_balance = customer_steps.customer_page.get_customer_balance()
        assert start_balance == end_balance, (
            f"Balance {end_balance} after deposit and withdrawl, but expected {start_balance}"
        )
        attach_csv_teardown(customer_steps.transactions_page.get_customer_transactions(transactions_count))
