import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def validate_profile_context(self, *args):
        """
        Validates that each given label appears on the profile screen
        as a content-desc of an element.

        :param labels: Strings of expected content-descriptions on the profile page
        """
        for label in args:
            logger.info(f"Validating existence of label: {label}")

            item = self.find_by_content_desc(desc=label)
            assert item is not None, f"Faild to find {label}"
            assert item.get_attribute("content-desc") == label
            logger.info(f"Successfully validated label: {label}")
