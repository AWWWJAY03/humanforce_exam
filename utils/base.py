import os
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_element(self, element):
        self.wait.until(ec.visibility_of_element_located(element)).click()

    def input_text(self, element, text: str):
        # element = self.wait.until(ec.visibility_of_element_located(element))
        locator = self.driver.find_element(*element)
        locator.clear()
        locator.send_keys(text)

    def get_text(self, element):
        locator = self.wait.until(ec.visibility_of_element_located(element))
        return locator.text

    def select_dropdown(self, element, options: str):
        locator = Select(self.wait.until(ec.visibility_of_element_located(element)))
        locator.select_by_value(options)

    def click_link_by_visible_text(self, link_text: str):
        element = (By.XPATH, f"//*[.='{link_text}']/a")
        self.wait_until_visible(element, 60)
        self.scroll_into_view(element)
        self.click_element(element)

    def scroll_into_view(self, element):
        locator = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)

    def is_element_visible(self, element):
        try:
            self.driver.find_element(*element).is_displayed()
            return True
        except NoSuchElementException:
            return False

    def wait_until_visible(self, element, timeout=30):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(element))

    def go_to_link(self, link):
        self.driver.get(f"{os.getenv('HUMANFORCE_LOGIN_PAGE')}/{link}")

