from common import Customers, TransactionType
from step.customers_steps import CustomersSteps
from utils.common_utils import get_amount
import pytest_check as check


class TestCustomer:
    def test_customer_debit_credit(self, customer_steps: CustomersSteps, attach_csv: None):
        """"""
        amount = get_amount()
        customer = Customers.HarryPotter
        customer_steps.login_as_customer(customer)
        start_balance = customer_steps.customer_page.get_customer_balance()
        customer_steps.check_transaction(amount=amount, transaction_type=TransactionType.deposit)
        customer_steps.check_transaction(amount=amount, transaction_type=TransactionType.withdrawl)
        end_balance = customer_steps.customer_page.get_customer_balance()
        check.equal(start_balance, end_balance)
        transactions = customer_steps.customer_page.get_customer_transactions()
