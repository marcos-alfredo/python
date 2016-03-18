# actions = ActionChains(driver)
# actions.double_click(search).perform()

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_001_open_tab(self):
        driver = self.driver
        driver.get("https://www.google.com")

        elem = driver.find_element_by_
        driver.send_keys(Keys.CONTROL, 't')

        expectedResult = "Google"

        self.assertIn(expectedResult, driver.title, "Expected: " +
                      expectedResult + " - Actual: " + driver.title)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
