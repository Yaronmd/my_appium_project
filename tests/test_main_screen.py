from pages.login_page import LoginPage
from pages.main_page import MainPage

    
    
    
    
def test_init_main_page(driver):
    
    user_name = "test@lumen.me"
    password =  "qwerty"
    login_page = LoginPage(driver)
    login_page.perfrom_login(user_name, password)
    main_page = MainPage(driver)
    
    title = main_page.get_title(user_name)
    
    assert title is not None
    assert title.get_attribute("content-desc") == f"Welcome {user_name}"
    
    
    
    
