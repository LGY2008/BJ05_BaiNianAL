from Base.get_driver import get_driver
from Page.page_login import PageLogin
from Page.page_address import PageAddress
class PageIn():
    def __init__(self):
        self.driver=get_driver()
    def page_get_login(self):
        return PageLogin(self.driver)
    def page_get_address(self):
        return PageAddress(self.driver)