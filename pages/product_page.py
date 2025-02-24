from pages.base_page import BasePage
from locators.product_pages_locators import *


class ProductPage(BasePage):

    def find_product_tiles(self):
        return self.page.locator(PRODUCT_TILE_LOCATOR).count()

    def click_burger(self):
        self.page.locator(selector=BURGER_LOCATOR).click()

    def find_all_items(self):
        self.page.locator(selector=BURGER_ALL_ITEMS_LOCATOR).is_visible()

    def find_about_item(self):
        self.page.locator(selector=BURGER_ABOUT_LOCATOR).is_visible()

    def find_logout_item(self):
        self.page.locator(selector=BURGER_LOGOUT_LOCATOR).is_visible()

    def find_reset_app_item(self):
        self.page.locator(selector=BURGER_RESET_APP_STATE).is_visible()
