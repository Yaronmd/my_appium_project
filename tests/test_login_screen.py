import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.parametrize("username,password", [("123", "123"), ("abcd", "abcd")])
def test_login_with_wrong_credentials(driver, username, password):
    """
    Try to log in with invalid credentials and verify that login fails.
    """
    login_page = LoginPage(driver)
    login_page.perfrom_login(username, password)

    main_page = MainPage(driver)
    actual_title = main_page.get_title(username)

    assert (
        actual_title != f"Welcome {username}"
    ), "User should not be able to log in with invalid credentials"


def test_login_without_credentials(driver):
    """
    Try to log in without providing any credentials and verify error messages are shown.
    """
    login_page = LoginPage(driver)
    login_page.perfrom_login("", "")

    login_page.get_username_field_message() == "Enter email"
    login_page.get_password_field_message() == "Enter password"
    login_page.get_fill_in_field_message() == "Please fill in all fields."
