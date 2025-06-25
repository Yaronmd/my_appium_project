from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    
    def get_title(self,username:str):
        return self.find_by_content_desc(desc=f"Welcome {username}")
        