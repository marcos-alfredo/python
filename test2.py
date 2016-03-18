import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_001_title(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

    def test_002_search(self):
        driver = self.driver
        driver.get("http://www.google.com")
        elem = driver.find_element_by_name("q")
        elem.send_keys("teste")
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertIn("Google", driver.title)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
