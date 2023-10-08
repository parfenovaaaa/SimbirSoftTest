import datetime
import re
from typing import List
import csv

from common import Customers
from page.customer_page import Transaction

file_name = f"{str(datetime.datetime.now()).replace(':', '-').split('.')[0]}.csv"


def create_transactions_csv(transactions: List[Transaction]) -> str:
    """"""
    with open(file_name, "w", newline='') as file:
        fields = ["Date-Time", "Amount", "Transaction type"]
        writer = csv.writer(file)
        writer.writerow(fields)
        for transaction in transactions:
            writer.writerow([transaction.date_time, transaction.amount, transaction.type])
        return file.name


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def get_amount() -> int:
    """"""
    today = int(datetime.date.today().day) + 1
    return fibonacci(today)
