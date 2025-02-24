from myRepo.lesson_16.locators.product_pages_locators import PRODUCT_TILE_LOCATOR
from myRepo.lesson_16.pages.product_page import ProductPage


class TestLoginPage:

    def test_hp(self, login_page):
        login_page.login(username="standard_user", password="secret_sauce")
        assert login_page.is_visible(locator="//span[@class='title']")

    def test_login_error_message(self, login_page):
        login_page.login(username="incorrect_username", password="incorrect_password")
        expected_error_message_text = "Epic sadface: Username is required"
        actual_error_message_text = login_page.get_login_error_message()
        if expected_error_message_text == actual_error_message_text:
            assert "Everything is OK", f"Should be {expected_error_message_text}, but got {actual_error_message_text}"

    def test_six_product_tiles(self, login_page, page):
        login_page.login(username="standard_user", password="secret_sauce")
        product_tiles = ProductPage(page)
        print(product_tiles.find_product_tiles())
        assert product_tiles.find_product_tiles() == 6, f"Returned {product_tiles.find_product_tiles()} product tile(s)"
