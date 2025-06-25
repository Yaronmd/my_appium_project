import pytest
from pages.login_page import LoginPage
from utils.driver_factory import get_driver

import os
from dotenv import load_dotenv

load_dotenv()



@pytest.fixture
def credentials():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }

@pytest.fixture(scope="function")
def driver():
    driver = get_driver("capabilities/android_caps.json")
    yield driver
    driver.quit()

@pytest.fixture
def login_app(driver,credentials):
  
    login_page = LoginPage(driver)
    login_page.perfrom_login(credentials["username"], credentials[password])