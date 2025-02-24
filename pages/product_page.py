from myRepo.pages.base_page import BasePage
from myRepo.locators.product_pages_locators import *


# def find_product_tile(locator: str, count: str):
#     expect(locator).toHaveCount(count)


class ProductPage(BasePage):

    def find_product_tiles(self):
        return self.page.locator(PRODUCT_TILE_LOCATOR).count()