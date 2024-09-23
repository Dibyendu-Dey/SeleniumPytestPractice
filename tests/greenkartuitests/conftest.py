import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# use the annotation @pytest.fixture to define a fixture function
# By default the fixture's scope is set to test method
# pass the request argument to make the driver object available to the test that uses the setup fixture.

@pytest.fixture(
    scope="class"
)  # setting the scope to class as we will encapsulate all the pytest test methods inside a class
def setup(request):
    try:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        # create a driver object
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(30)
        # code to load the URl
        driver.get(url="r")
        # make the driver object available to the test that uses the fixture setup.
        request.cls.driver = driver  # here we make the driver object available as an argument driver within the tests.
        print("The page is loaded successfully")
        yield
        driver.close()
    except Exception as e:
        print(f"Error Occurred: {e}")
