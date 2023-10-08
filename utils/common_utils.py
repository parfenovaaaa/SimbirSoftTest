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
    date_time: str
    amount: int
    type: str
