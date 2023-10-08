import datetime
from dataclasses import dataclass


def fibonacci(n: int) -> int:
    """
    Evaluate fibonacci number of n
    """
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def get_amount() -> int:
    """
    Get amount for today
    """
    today = int(datetime.date.today().day) + 1
    return fibonacci(today)


TIME_TEMPLATE = "%b %d, %Y %H:%M:%S %p"


def date_str_to_date(date_str: str) -> datetime:
    """
    Create datetime from str
    """
    return datetime.datetime.strptime(date_str, TIME_TEMPLATE)


class Customers:
    HarryPotter = "Harry Potter"


class TransactionType:
    deposit = "Deposit"
    withdrawl = "Transaction"


TransactionMessage = {
    TransactionType.deposit: "Deposit Successful",
    TransactionType.withdrawl: "Transaction successful"
}


@dataclass
class Transaction:
    date_time: datetime
    amount: int
    type: str
