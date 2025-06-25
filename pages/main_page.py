import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

logger = logging.getLogger(__name__)


class MainPage(BasePage):

    myCounterlabel = (By.XPATH, "//android.view.View[@content-desc='My Counter']")
    countNumber = (
        By.XPATH,
        "(//android.view.View[contains(@content-desc,'My Counter')]/following-sibling::android.view.View)[1]",
    )
    resetButton = "Reset Counter"

    homeTabButton = "Home\nTab 1 of 3"
    messagesTabButton = "Messages\nTab 2 of 3"
    profileTabButton = "Profile\nTab 3 of 3"

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self, username: str):
        """
        Get the welcome title containing the username.

        :param username: The expected username
        :return: The title text
        """
        logger.info(f"Getting title for user: {username}")
        title = self.find_by_content_desc(desc=f"Welcome {username}")
        assert title is not None
        return title.get_attribute("content-desc")

    def validate_my_counter_label(self):
        """
        Validate that the 'My Counter' label exists and return its text.
        """
        logger.info("Validating 'My Counter' label")
        counter_label = self.find_by_content_desc(desc=f"My Counter")
        assert counter_label is not None
        return counter_label.get_attribute("content-desc")

    def get_count_number(self):
        """
        Get the current number shown in the counter.

        :return: The number as string from content-desc
        """
        logger.info("Getting count number")
        counter_number = self.find_element(self.countNumber)
        assert counter_number is not None
        return counter_number.get_attribute("content-desc")

    def click_reset_button(self):
        """
        Click the 'Reset Counter' button.
        """
        logger.info("Clicking reset counter button")
        reset_button = self.find_by_content_desc(self.resetButton)
        assert reset_button is not None
        reset_button.click()

    def click_home_tab_button(self):
        """
        Click the Home tab button.
        """
        logger.info("Clicking home tab button")
        home_button = self.find_by_content_desc(self.homeTabButton)
        assert home_button is not None
        home_button.click()

    def click_messages_tab_button(self):
        """
        Click the Messages tab button.
        """
        logger.info("Clicking messages tab button")
        msg_button = self.find_by_content_desc(self.messagesTabButton)
        assert msg_button is not None
        msg_button.click()

    def click_profile_tab_button(self):
        """
        Click the Profile tab button.
        """
        logger.info("Clicking profile tab button")
        profile_button = self.find_by_content_desc(self.profileTabButton)
        assert profile_button is not None
        profile_button.click()
