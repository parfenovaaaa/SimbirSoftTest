from dataclasses import dataclass


class TransactionType:
    deposit = "Deposit"
    withdrawl = "Transaction"


TransactionMessage = {
    TransactionType.deposit: "Deposit Successful",
    TransactionType.withdrawl: "Transaction successful"
}


class Customers:
    HarryPotter = "Harry Potter"


@dataclass
class Transaction:
    date_time: str
    amount: int
    type: str
