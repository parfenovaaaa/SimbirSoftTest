import csv
from datetime import datetime
from typing import Dict

import allure
import pytest
from _pytest.reports import CollectReport
from _pytest.stash import StashKey
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.customer_page import CustomerPage
from page.login_page import LoginPage
from step.customers_steps import CustomersSteps
from utils.common_utils import file_name

phase_report_key = StashKey[Dict[str, CollectReport]]()


@pytest.fixture(autouse=True)
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(
        command_executor='http://192.168.0.107:4444/wd/hub',
        options=options,
    )
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver: WebDriver) -> LoginPage:
    yield LoginPage(driver)


@pytest.fixture()
def customer_page(driver: WebDriver) -> CustomerPage:
    yield CustomerPage(driver)


@pytest.fixture()
def customer_steps(driver: WebDriver) -> CustomersSteps:
    yield CustomersSteps(driver)


@pytest.fixture
def attach_csv() -> None:
    transactions = []
    yield transactions
    with open(file_name, "w", newline='') as file:
        fields = ["Date-Time", "Amount", "Transaction type"]
        writer = csv.writer(file)
        writer.writerow(fields)
        for transaction in transactions:
            writer.writerow([transaction.date_time, transaction.amount, transaction.type])
        csv_file = file.name
    allure.attach(
        csv_file,
        attachment_type=AttachmentType.CSV
    )


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    rep = yield
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep
    return rep


@pytest.fixture(autouse=True)
def test_teardown(driver: WebDriver, request) -> None:
    yield
    report = request.node.stash[phase_report_key]
    if report["setup"].failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{str(datetime.now()).replace(':', '-').split('.')[0]}",
            attachment_type=AttachmentType.PNG
        )
