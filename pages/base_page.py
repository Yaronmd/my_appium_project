from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            print(f"Timeout: Element not clickable - {locator}")

    def send_keys(self, locator, text, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            print(f"Timeout: Element not found for send_keys - {locator}")

    def find_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except (TimeoutException, NoSuchElementException):
            print(f"Element not found - {locator}")
            return None

    def find_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except (TimeoutException, NoSuchElementException):
            print(f"Elements not found - {locator}")
            return []

    def find_by_content_desc(self, desc: str, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{desc}")')
            )
        except Exception as e:
            print(f"Element with content-desc '{desc}' not found: {e}")
            return None
        
    def wait_for_focus(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).get_attribute("focused") == "true"
            )
        except TimeoutException:
            print(f"Timeout: Element did not gain focus - {locator}")