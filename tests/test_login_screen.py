from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.perfrom_login("123",123)
    
    
    
    
def test_login_without_credentials(driver):
    login_page = LoginPage(driver)
    login_page.perfrom_login("", "")
    
    email_field = login_page.get_username_field_message()
    password_field = login_page.get_password_field_message()
    error_msg = login_page.get_fill_in_field_message()

    assert email_field is not None
    assert email_field.get_attribute("content-desc") == "Enter email"

    assert password_field is not None
    assert password_field.get_attribute("content-desc") == "Enter password"

    assert error_msg is not None
    assert error_msg.get_attribute("content-desc") == "Please fill in all fields."
    
    
    
    
