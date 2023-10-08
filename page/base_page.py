from typing import List, Union, Tuple

import pytest_check
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

ERROR = "Can't find element by locator {}"


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/"

    def open(self, page_url_part: str = None) -> None:
        """
        Open page by base url + optional url part
        """
        self.driver.get(f"{self.base_url}{page_url_part}")
        self.driver.execute_async_script("""window.requestIdleCallback(arguments[0], {timeout: 60000});""")

    def find_element(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Find Selenium element with wait
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator), message=ERROR.format(locator)
        )

    def find_elements(self, locator: Tuple[str, str], timeout: int = 10) -> List[WebElement]:
        """
        Find Selenium elements with wait
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator), message=ERROR.format(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Can't find element with locator {locator} on page {self.driver.current_url}")

    def fill_web_element(self, locator: Tuple[str, str], data: Union[str, int]) -> None:
        """
        Find Selenium input element with wait, clear it and fill with provided data
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(str(data))
        pytest_check.equal(element.get_attribute("value"), str(data))

    def click_web_element(self, locator: Tuple[str, str]) -> None:
        """
        Find Selenium element with wait and click it
        """
        element = self.find_element(locator)
        element.click()

    def select_web_element_option(self, locator: Tuple[str, str], value: str = None, text: str = None) -> None:
        """
        Find Selenium select element with wait, select by provided data
        """
        element = Select(self.find_element(locator))
        if value:
            element.select_by_value(value)
            return
        if text:
            element.select_by_visible_text(text)
            return
        raise EOFError
