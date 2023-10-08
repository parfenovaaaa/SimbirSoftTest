from typing import List, Union

import pytest_check
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ERROR = "Can't find element by locator {}"


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"

    def open(self, page_url_part: str = None) -> None:
        """"""
        self.driver.get(f"{self.base_url}{page_url_part}")
        self.driver.execute_async_script("""window.requestIdleCallback(arguments[0], {timeout: 60000});""")

    def find_element(self, locator, timeout: int = 10) -> WebElement:
        """"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator), message=ERROR.format(locator)
        )

    def find_elements(self, locator, timeout: int = 10) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator), message=ERROR.format(locator)
        )

    def fill_web_element(self, locator, data: Union[str, int]) -> None:
        element = self.find_element(locator)
        element.clear()
        element.send_keys(str(data))
        pytest_check.equal(element.get_attribute("value"), str(data))

    def click_web_element(self, locator) -> None:
        element = self.find_element(locator)
        element.click()

    def select_web_element_option(self, locator, value: str = None, text: str = None) -> None:
        element = Select(self.find_element(locator))
        if value:
            element.select_by_value(value)
            return
        if text:
            element.select_by_visible_text(text)
            return
        raise EOFError
