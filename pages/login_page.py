from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
    
    __usernameField = (By.XPATH,"//android.widget.EditText[1]")
    __passwordField =(By.XPATH,"//android.widget.EditText[2]")
    __loginButton = (By.CLASS_NAME,"android.widget.Button")
    
    def __init__(self, driver):
        super().__init__(driver)

    
    def enter_username(self,username:str):
        self.click(self.__usernameField)
        self.wait_for_focus(self.__usernameField)
        self.send_keys(locator=self.__usernameField,text=username)
        
    def enter_password(self,password:str):
        self.click(self.__passwordField)
        self.send_keys(locator=self.__passwordField,text=password)

    def click_login(self):
        print("Click login")
        self.click(self.__loginButton)
    
    
    def perfrom_login(self,username:str,password:str):
        self.enter_username(username=username)
        self.enter_password(password=password)
        self.click_login()
    
    def get_username_field_message(self):
        return self.find_by_content_desc(desc="Enter email")
    
    def get_password_field_message(self):
        return self.find_by_content_desc(desc="Enter password")
    
    def get_fill_in_field_message(self):
        return self.find_by_content_desc(desc="Please fill in all fields.")