import logging
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class MessagesPage(BasePage):

    messages_locator = (
        By.XPATH,
        '//android.view.View[starts-with(@content-desc, "Message from ")]',
    )

    def __init__(self, driver):
        super().__init__(driver)

    def get_all_messages(self):
        """
        Find and return all message elements in the Messages tab.

        :return: List of message WebElement objects
        """
        logger.info("Fetching all messages from Messages tab")
        messages = self.find_elements(self.messages_locator)
        assert messages is not None
        logger.info(f"Found {len(messages)} messages")
        return messages
