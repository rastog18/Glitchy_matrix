from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ------------------------------- Selenium Setup ---------------------------------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cursor = driver.find_element(By.XPATH, "//*[@id='cookie']")


# ------------------------------------ MAIN --------------------------------------#
def check_for_items(list_items):
    list_grayed_items = driver.find_elements(By.CLASS_NAME, "grayed")  # List of items that are not yet unlocked.
    list_grayed_items = [item.text.split(" -")[0] for item in list_grayed_items]

    list_clickable_items = list_items[0:list_items.index(list_grayed_items[0])]   # List of items that are unlocked.
    item = "buy" + list_clickable_items[-1]

    buy_item = driver.find_element(By.ID, item) # Locating the item we wish to buy
    buy_item.click()


list_items = driver.find_element(By.ID, "store").text.split("\n")
list_items = [item.split(" -")[0] for item in list_items if list_items.index(item) % 2 == 0]
break_time = int(time.time()) + (5 * 60)
time_init_sec = int(time.time())

while (time_init_sec < break_time):
    time_final_sec = int(time.time())
    cursor.click()
    if (time_final_sec == time_init_sec + 5):
        check_for_items(list_items)
        time_init_sec = int(time.time())
print(driver.find_element(By.ID, "cps").text)
driver.quit()
