import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy


logger = logging.getLogger(__name__)


class BasePage:
    """
    A base class for all screens.
    Includes common methods like click, find elements, send keys, etc.
    """

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        """
        Click on an element when it becomes clickable.

        :param locator: Tuple like (By.ID, "some_id")
        :param timeout: How long to wait for the element
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            logger.info(f"Clicked on element: {locator}")
        except TimeoutException:
            logger.exception(f"Timeout: Element not clickable - {locator}")
            raise

    def send_keys(self, locator, text, timeout=10):
        """
        Send text to an input element.

        :param locator: Tuple for locating the element
        :param text: Text to type
        :param timeout: How long to wait for the element
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            logger.info(f"Send keys on element: {locator}")
        except TimeoutException:
            logger.exception(f"Timeout: Element not found for send_keys - {locator}")
            raise

    def find_element(self, locator, timeout=10):
        """
        Find one element.

        :param locator: Tuple to find the element
        :param timeout: Wait time
        :return: The found element or None
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except (TimeoutException, NoSuchElementException):
            logger.exception(f"Element not found - {locator}")
            return None

    def find_elements(self, locator, timeout=10):
        """
        Find a list of elements.

        :param locator: Tuple to find elements
        :param timeout: Wait time
        :return: List of elements (could be empty)
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except (TimeoutException, NoSuchElementException):
            logger.exception(f"Elements not found - {locator}")
            return []

    def find_by_content_desc(self, desc: str, timeout=10):
        """
        Find element using content-desc (accessibility ID).

        :param desc: The content-desc value
        :param timeout: Wait time
        :return: The found element or None
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().description("{desc}")',
                )
            )
        except Exception as e:
            logger.exception(f"Element with content-desc '{desc}' not found: {e}")
            return None

    def wait_for_focus(self, locator, timeout=10):
        """
        Wait until the element gets focus.

        :param locator: Tuple to find the element
        :param timeout: Wait time
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).get_attribute("focused") == "true"
            )
        except TimeoutException:
            logger.exception(f"Timeout: Element did not gain focus - {locator}")

    def logout(self):
        """
        Try to click the logout button using two fallback locators.
        Logs success or failure.
        """
        try:
            logout_btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.Button").instance(0)',
            )
            logout_btn.click()
            logger.info("Success to logout")
        except Exception:
            try:
                logout_btn = self.driver.find_element(
                    AppiumBy.XPATH,
                    '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button',
                )
                logout_btn.click()
            except Exception as e:
                raise Exception("Failed to locate and click the logout button") from e
