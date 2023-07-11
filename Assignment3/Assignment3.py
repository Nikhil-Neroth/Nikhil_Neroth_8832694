
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()


# Navigating to the canadian tire homepage
driver.get("https://www.canadiantire.ca/en.html")
time.sleep(6)
driver.maximize_window()
time.sleep(2)
# Finding the search bar and entering text
search_bar = driver.find_element("id","search-input-0")
time.sleep(5)
search_bar.send_keys("Cycles")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

driver.execute_script("window.scrollBy(0,300)","")
# select the product to buy
product_Link=driver.find_element(By.XPATH,value="//div[@id='title__search-071-1908-6']")
time.sleep(5)
product_Link.click()
driver.execute_script("window.scrollBy(0,300)","")
time.sleep(4)

# add the products to the cart
add_cart=driver.find_element("id","add-to-cart")
time.sleep(4)
add_cart.click()
time.sleep(3)

# Proceed to checkout page
continue_cart=driver.find_element("id","footer-btn")
continue_cart.click()
time.sleep(4)
driver.execute_script("window.scrollBy(0,700)","")

# continue to check out page
driver.execute_script("window.scrollBy(0,300)","")
check_out=driver.find_element("xpath","/html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div/div/span/div/div/div[5]/button")
check_out.click()
time.sleep(8)
# # Closing the webdriver
driver.close()
