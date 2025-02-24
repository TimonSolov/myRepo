from myRepo.pages.base_page import BasePage
from myRepo.locators.main_pages_locators import *


class LoginPage(BasePage):

    def login(self, username: str, password: str):
        self.fill_text(USERNAME_FIELD, text=username)
        self.fill_text(locator=PASSWORD_FIELD_LOCATOR, text=password)
        self.click(locator=LOGIN_BUTTON)

    def get_login_error_message(self):
        return self.get_text(locator=ERROR_MESSAGE)
