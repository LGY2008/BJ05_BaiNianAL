from Page.page_login import PageLogin
from Page.page_address import PageAddress
class PageIn():
    def __init__(self,driver):
        self.driver=driver
    def page_get_login(self):
        return PageLogin(self.driver)
    def page_get_address(self):
        return PageAddress(self.driver)