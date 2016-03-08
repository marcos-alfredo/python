import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        driver = self.driver
        driver.get("https://www.google.com")

        expectedResult = "Google"

        self.assertIn(expectedResult, driver.title, "Expected: " + expectedResult + " - Actual: " + driver.title)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        while driver.execute_script("return document.readyState;") != "complete":
            time.sleep(1)
        searchBox = driver.find_element_by_name("q")
        searchBox.click()
        searchBox.send_keys("teste")
        time.sleep(1)
        searchBox.send_keys(Keys.RETURN)
        time.sleep(2)

        expectedResult = "teste"

        self.assertIn(expectedResult, driver.title, "Expected: " + expectedResult + " - Actual: " + driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
