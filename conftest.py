import pytest
from utils.driver_factory import get_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver("capabilities/android_caps.json")
    yield driver
    driver.quit()
