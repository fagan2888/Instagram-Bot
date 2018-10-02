## INPUTS ##
#=============================================================================+#
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## OPEN BROWSER ##
#=============================================================================+#
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')

## LOGIN ##
#=============================================================================+#
driver.implicitly_wait(5) # seconds
username = driver.find_element_by_name("username")
username.click();
username2 = driver.find_element_by_name("username")
username2.send_keys("") # USERNAME
driver.implicitly_wait(5)

password = driver.find_element_by_name("password")
password.click();
password2 = driver.find_element_by_name("password")
password2.send_keys("") # PASSWORD

logLink = driver.find_element_by_tag_name('button')
logLink.click()

## WAIT ##
#=============================================================================+#
driver.implicitly_wait(5)
time.sleep(2)

driver.refresh()
time.sleep(2)

## UNFOLLOW CODE ##
#=============================================================================+#
numToUnfollow = 100;

for y in range(numToUnfollow):

    # Go to your profile page.
    driver.get('https://www.instagram.com/in.st.art/') # THIS IS HARD CODED
    time.sleep(2)

    try:
        # Click on followers.
        following = driver.find_elements_by_xpath("//header/section/ul/li[3]/a")
        following[0].click()
        time.sleep(2)

        # Unfollow person.
        string = "//div[@role='dialog']/div[2]/div/div[2]/ul/div/li/div/div[2]/button"
        person = driver.find_elements_by_xpath(string)
        person[0].click()
        time.sleep(2)

    except Exception as e:
        print "Failed to unfollow."
        raise
