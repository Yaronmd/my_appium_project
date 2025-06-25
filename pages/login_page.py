import logging
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):

    usernameField = (By.XPATH, "//android.widget.EditText[1]")
    passwordField = (By.XPATH, "//android.widget.EditText[2]")
    loginButton = (By.CLASS_NAME, "android.widget.Button")

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_title(self):
        """
        Get the login page title (from content-desc).
        """
        logger.info("Getting login title")
        login_title = self.find_by_content_desc("Login")
        return login_title.get_attribute("content-desc")

    def enter_username(self, username: str):
        """
        Enter the username into the input field.

        :param username: The username to type
        """
        logger.info(f"Entering username: {username}")
        self.click(self.usernameField)
        self.wait_for_focus(self.usernameField)
        self.send_keys(locator=self.usernameField, text=username)

    def enter_password(self, password: str):
        """
        Enter the password into the input field.

        :param password: The password to type
        """
        logger.info(f"Entering password: {'*' * len(password)}")
        self.click(self.passwordField)
        self.send_keys(locator=self.passwordField, text=password)

    def click_login(self):
        """
        Click the login button.
        """
        logger.info("Click login")
        self.click(self.loginButton)

    def perfrom_login(self, username: str, password: str):
        """
        Fill in the login form and submit.

        :param username: User's username
        :param password: User's password
        """
        logger.info("Performing login flow")
        self.enter_username(username=username)
        self.enter_password(password=password)
        self.click_login()

    def get_username_field_message(self):
        """
        Get the message shown under the username field (e.g. 'Enter email').

        :return: The content-desc message
        """
        logger.info("Checking email field message")
        email_field = self.find_by_content_desc(desc="Enter email")
        assert email_field is not None
        if email_field:
            return email_field.get_attribute("content-desc")

    def get_password_field_message(self):
        """
        Check if the correct message appears for the password field.

        :return: True if message matches expected
        """
        logger.info("Checking password field message")
        password_field = self.find_by_content_desc(desc="Enter password")
        assert password_field is not None
        return password_field.get_attribute("content-desc") == "Enter password"

    def get_fill_in_field_message(self):
        """
        Get the message when required fields are left empty.

        :return: The content-desc of the error message
        """
        logger.info("Getting error message for empty fields")
        error_msg = self.find_by_content_desc(desc="Please fill in all fields.")
        assert error_msg is not None
        return error_msg.get_attribute("content-desc")
