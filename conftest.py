import datetime
import logging
import pytest
from pages.login_page import LoginPage
from utils.driver_factory import get_driver

import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def credentials():
    return {"username": os.getenv("USERNAME"), "password": os.getenv("PASSWORD")}


@pytest.fixture(scope="function")
def driver():
    driver = get_driver("capabilities/android_caps.json")
    yield driver
    driver.quit()


@pytest.fixture
def login_app(driver, credentials):

    login_page = LoginPage(driver)
    login_page.perfrom_login(credentials["username"], credentials["password"])

    return login_page


@pytest.fixture(autouse=True, scope="session")
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(
                "screenshots", datetime.now().strftime("%Y-%m-%d")
            )
            os.makedirs(screenshots_dir, exist_ok=True)

            test_name = item.name.replace("/", "_").replace("::", "_")
            filename = f"{test_name}_{datetime.now().strftime('%H-%M-%S')}.png"
            filepath = os.path.join(screenshots_dir, filename)

            driver.save_screenshot(filepath)
            logging.error(f"Screenshot saved to: {filepath}")
