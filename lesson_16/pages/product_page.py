from myRepo.lesson_16.pages.base_page import BasePage
from myRepo.lesson_16.locators.main_pages_locators import *
from myRepo.lesson_16.locators.product_pages_locators import *


# def find_product_tile(locator: str, count: str):
#     expect(locator).toHaveCount(count)


class ProductPage(BasePage):

    def find_product_tiles(self):
        return self.page.locator(PRODUCT_TILE_LOCATOR).count()