from typing import List, Union

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from utils.common_utils import Transaction, date_str_to_date


class TransactionsPage(BasePage):
    page_url_part = "#/listTx"

    transaction_table = (By.CSS_SELECTOR, "tbody tr")

    def get_customer_transactions(self, expected_count: int) -> Union[str, List[Transaction]]:
        """
        Open customer transactions page, check amount of transactions and return them
        """
        self.open(self.page_url_part)
        count = len(self.find_elements(self.transaction_table))
        assert count == expected_count, f"Expected to see {expected_count} transactions, but found {count}"
        transactions = []
        for row in self.find_elements(self.transaction_table):
            data = row.find_elements(By.TAG_NAME, "td")
            transaction = Transaction(
                date_time=date_str_to_date(data[0].text), amount=int(data[1].text), type=data[2].text
            )
            transactions.append(transaction)
        return transactions
