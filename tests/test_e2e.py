from pages.main_page import MainPage
from pages.messages_page import MessagesPage
from pages.profile_page import ProfilePage


def test_init_main_page(driver, login_app, credentials):
    """
    Verify the main page is initialized correctly after login.
    Checks the welcome title, counter label, and initial counter value.
    """
    main_page = MainPage(driver)
    username = credentials["username"]
    assert main_page.get_title(username) == f"Welcome {username}"
    assert main_page.validate_my_counter_label() == "My Counter"
    assert main_page.get_count_number() == "0"


def test_counter_increase_and_reset(driver, login_app):
    """
    Verify that the counter increases when navigating to the home tab,
    and resets to 0 when clicking the reset button.
    """
    main_page = MainPage(driver)
    assert main_page.get_count_number() == "0"
    main_page.click_home_tab_button()
    assert main_page.get_count_number() == "1"
    main_page.click_reset_button()
    assert main_page.get_count_number() == "0"


def test_naviagte_messages_page(driver, login_app):
    """
    Verify navigation to the messages tab and that at least one message is displayed.
    """
    main_page = MainPage(driver)
    main_page.click_messages_tab_button()
    msg_page = MessagesPage(driver)
    assert len(msg_page.get_all_messages()) >= 1


def test_naviagte_profile_page(driver, login_app):
    """
    Verify navigation to the profile tab and that all profile information is displayed.
    """
    main_page = MainPage(driver)
    main_page.click_profile_tab_button()
    proflie_page = ProfilePage(driver)
    proflie_page.validate_profile_context(
        "Peter Pan",
        "Address: Pixie Hollow, Neverland",
        "Second star to the right, and straight on till morning!",
    )


def test_logout_from_main_page(driver, login_app):
    """
    Verify that the user can log out successfully from the main page.
    """
    main_page = MainPage(driver)
    main_page.logout()
    login_app.get_login_title()


def test_logout_from_profile_page(driver, login_app):
    """
    Verify that the user can log out successfully from the profile page.
    """
    main_page = MainPage(driver)
    main_page.click_profile_tab_button()
    proflie_page = ProfilePage(driver)
    proflie_page.logout()
    login_app.get_login_title()


def test_logout_from_messages_page(driver, login_app):
    """
    Verify that the user can log out successfully from the messages page.
    """
    main_page = MainPage(driver)
    main_page.click_profile_tab_button()
    msg_page = MessagesPage(driver)
    msg_page.logout()
    login_app.get_login_title()
