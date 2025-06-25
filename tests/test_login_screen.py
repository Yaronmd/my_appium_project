from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.perfrom_login("123",123)
    
    
    
    
def test_login_without_credentials(driver):
    login_page = LoginPage(driver)
    login_page.perfrom_login("", "")
    
    login_page.get_username_field_message() == "Enter email"
    login_page.get_password_field_message() == "Enter password"
    login_page.get_fill_in_field_message() == "Please fill in all fields."
    
 

   
    
    
    
    
