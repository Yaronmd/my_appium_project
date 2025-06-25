import json
from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver(cap_file_path: str):
    with open(cap_file_path) as f:
        caps = json.load(f)

    options = UiAutomator2Options().load_capabilities(caps)

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
    return driver
