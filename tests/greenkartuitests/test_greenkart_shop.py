import time
import allure
from allure_commons.types import AttachmentType
from PageObjects.GreenKartPageObjects.shoppage import *
import pytest


@pytest.mark.usefixtures("setup")
class TestGreenKartShopPage:
    @pytest.mark.parametrize("item_name", ["Strawberry"])
    def test_add_items(self, setup, item_name):
        shop_page = ShopPage(driver=self.driver)
        print("Locating the search Bar")
        shop_page.go_to_search_bar()
        print(f"Searching the item {item_name}")  # uses f-string format to format and print the string
        shop_page.search_for_veggies_fruits(item_name)
        time.sleep(5)
        print(f"Adding the item {item_name} to the cart")
        shop_page.compare_item_name(item_name)
        # To take screenshot in allure report
        allure.attach(self.driver.get_screenshot_as_png(), name="add_veggies", attachment_type=AttachmentType.PNG)
