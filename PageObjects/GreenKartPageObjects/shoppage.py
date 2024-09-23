from selenium.webdriver.common.by import By


class ShopPage:
    # class variable
    search_bar = (By.CSS_SELECTOR, "input.search-keyword")
    item_name = (By.XPATH, "//div/h4")

    # add_to_cart_button = (By.XPATH, "//button[text()='ADD TO CART']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_search_bar(self):
        """Locates the search bar"""
        self.driver.find_element(*self.search_bar)

    def search_for_veggies_fruits(self, item_name):
        self.driver.find_element(*self.search_bar).send_keys(item_name)
        self.driver.find_element(*self.search_bar).clear()

    def get_item_name(self):
        return self.driver.find_element(*self.item_name).text

    def compare_item_name(self, expected_name):
        actual_name = self.get_item_name()
        actual_name = actual_name.split(" ")[0]
        if expected_name == actual_name:
            print("Match")
        else:
            print("Not Match")
            raise Exception(f"{expected_name} is not equal to {actual_name}")
