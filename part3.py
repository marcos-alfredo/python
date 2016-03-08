import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(1)

search = driver.find_element_by_name("q")

search.send_keys("teste")
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(2)
actions = ActionChains(driver)
actions.double_click(search).perform()
time.sleep(2)

# actions.drag_and_drop(search, bar).perform()

driver.close()
driver.quit()
