from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ------------------------------- Variable and Constats ---------------------------------#

linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=3708954318&f_LF=f_AL&geoId=103336534&keywords=python%20developer&location=Indiana%2C%20United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"
linkedin_usr = "*********"
linkedin_pass = "*********"
phone_number = 1234567890
# ------------------------------- Selenium Setup ---------------------------------#
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(linkedin_url)
driver.maximize_window()
# TODO -1: Signing in Linkedin.
time.sleep(4)
signin_tag = driver.find_element(By.XPATH,"/html/body/div[3]/a[1]")
signin_tag.click()

time.sleep(3)
email_box = driver.find_element(By.ID,"username")
email_box.send_keys(linkedin_usr)

time.sleep(2)
email_box = driver.find_element(By.ID,"password")

time.sleep(1)
email_box.send_keys(linkedin_pass,Keys.ENTER)

input("Please Enter if you have entered the verification code.")

# TODO-2: Easy Applying to jobs.
time.sleep(1)
job_div = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div')
time.sleep(1) # Beacuse of Lazy loading of Elements
driver.execute_script("arguments[0].scrollTop += 1000;", job_div)
time.sleep(1) # Beacuse of Lazy loading of Elements
driver.execute_script("arguments[0].scrollTop += 1000;", job_div)
time.sleep(1) # Beacuse of Lazy loading of Elements
driver.execute_script("arguments[0].scrollTop += 1000;", job_div)
time.sleep(4)

job_list = driver.find_elements(By.CSS_SELECTOR,".job-card-list__title")
for job in job_list:
    job.click()
    time.sleep(1)

    apply_icon = driver.find_element(By.CSS_SELECTOR,".jobs-apply-button--top-card button")
    apply_icon.click()

    phone_input_icons = driver.find_elements(By.CSS_SELECTOR,".artdeco-text-input--input")
    phone_input_icon = phone_input_icons[-1]
    phone_input_icon.send_keys(phone_number)
    next_icon = driver.find_element(By.CSS_SELECTOR,".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
    next_icon.click()
    input("Enter if you have further filled the details.")
    # Beyond this point usually each on of the applications is different.

time.sleep(4)
print(f"You have submitted {len(job_list)} applications.")
driver.close()
