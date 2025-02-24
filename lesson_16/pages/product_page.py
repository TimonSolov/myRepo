from saucedemo_test.pages.base_page import BasePage
from saucedemo_test.locators.main_page_locators import *
from saucedemo_test.locators.product_page_locators import *


# def find_product_tile(locator: str, count: str):
#     expect(locator).toHaveCount(count)


class ProductPage(BasePage):

    def find_product_tiles(self):
        return self.page.locator(PRODUCT_TILE_LOCATOR).count()