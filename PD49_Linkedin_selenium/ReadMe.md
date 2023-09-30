# LinkedIn Easy Apply Automation

This script is designed to automate the process of applying to multiple jobs on LinkedIn with ease. It uses the Selenium web automation framework in Python to navigate to LinkedIn, sign in to your account, and apply to job listings. Before using this script, make sure you have the necessary dependencies installed:

# Dependencies:
### 1. Selenium: You can install it using `pip`:
```pip install selenium```

### 2. Chrome WebDriver: You need to have the Chrome WebDriver executable installed. Make sure it's compatible with your Chrome browser version. You can download it from the official ChromeDriver website: https://sites.google.com/chromium.org/driver/

### 3. LinkedIn Account: You should have a LinkedIn account with your login credentials.

# Usage Instructions:

### 1. Update the following variables in the script with your LinkedIn credentials and preferences:

    - `linkedin_url`: The URL of the LinkedIn job search page.
    - `linkedin_usr`: Your LinkedIn email address.
    - `linkedin_pass`: Your LinkedIn password.
    - `phone_number`: Your phone number for job applications.
   
###    You can customize the `linkedin_url` variable to filter job listings according to your preferences.

### 2. Execute the script using Python:
```python script_name.py```

### 3. The script will open a Chrome browser window, navigate to LinkedIn, sign in, and then automatically apply to jobs.

### 4. After running the script, you will be prompted to enter a verification code if LinkedIn requires it for sign-in.

### 5. The script will scroll down to load more job listings, click on each job listing, and initiate the application process.

### 6. You will be prompted to enter additional information for each job application.

### 7. Continue this process until you have applied to all the desired jobs.

### 8. The script will display the number of job applications submitted, and you can close the browser window.

## Note: The script is designed for educational purposes and should be used responsibly. LinkedIn's policies may change over time, so ensure that you are compliant with their terms of service when using automation scripts. Be cautious not to violate any rules or engage in spammy behavior.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# #---------------- Variables and Constants ----------------#

### Define your LinkedIn URL, email, password, and phone number here
- linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=3708954318&f_LF=f_AL&geoId=103336534&keywords=python%20developer&location=Indiana%2C%20United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"
- linkedin_usr = "your_linkedin_email@gmail.com"
- linkedin_pass = "your_linkedin_password"
- phone_number = 1234567890



time.sleep(4)
print(f"You have submitted {len(job_list)} applications.")
driver.close()
