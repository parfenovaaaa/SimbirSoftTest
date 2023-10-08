import csv
from datetime import datetime
from typing import Dict, Callable, List, Any

import allure
import pytest
from _pytest.fixtures import SubRequest
from _pytest.reports import CollectReport
from _pytest.stash import StashKey
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from utils.common_utils import Transaction
from step.customers_steps import CustomersSteps

PHASE_REPORT_KEY = StashKey[Dict[str, CollectReport]]()
ALLURE_FILE = f"{str(datetime.now()).replace(':', '-').split('.')[0]}"


@pytest.fixture(autouse=True)
def driver(request: SubRequest) -> WebDriver:
    """
    Set up webdriver before test and return it
    After test make screenshot if failed and close browser
    """
    options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options,
    )
    yield driver
    if request.node.stash[PHASE_REPORT_KEY]["call"].failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{ALLURE_FILE}_screenshot",
            attachment_type=AttachmentType.PNG
        )
    driver.quit()


@pytest.fixture()
def customer_steps(driver: WebDriver) -> CustomersSteps:
    """
    Steps for customers actions
    """
    yield CustomersSteps(driver)


@pytest.fixture
def attach_csv_teardown() -> Callable:
    """
    Create csv file of transactions and attach them to allure report
    """
    def _attach_csv(transactions: List[Transaction]) -> None:
        file_name = f"{str(datetime.now()).replace(':', '-').split('.')[0]}.csv"
        with open(file_name, "w", newline='') as file:
            fields = ["Date-Time", "Amount", "Transaction type"]
            writer = csv.writer(file)
            writer.writerow(fields)
            [writer.writerow([tx.date_time, tx.amount, tx.type]) for tx in transactions]
        with open(file_name, 'rb') as f:
            allure.attach(f.read(), name=f"{ALLURE_FILE}_transactions", attachment_type=AttachmentType.CSV)
        return
    return _attach_csv


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item) -> Any:
    """
    makereport to  catch failed tests
    """
    rep = yield
    item.stash.setdefault(PHASE_REPORT_KEY, {})[rep.when] = rep
    return rep
