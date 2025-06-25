from pages.login_page import LoginPage
from pages.main_page import MainPage

    
    
    
    
def test_init_main_page(driver,login_app,credentials):
    main_page = MainPage(driver)
    username = credentials["username"]
    assert main_page.get_title(username) == f"Welcome {username}"
    assert main_page.validate_my_counter_label() == "My Counter"
    assert main_page.get_count_number() == "0"
    assert main_page.validate_bottom_nav_bar_exists()
    
    
    
    
def test_counter_increase_and_reset(driver,login_app):
    main_page = MainPage(driver)
    assert main_page.get_count_number() == "0"
    main_page.click_home_tab_button()
    assert main_page.get_count_number() == "1"
    main_page.click_reset_button()
    assert main_page.get_count_number() == "0"
    
    
