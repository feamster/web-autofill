#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select

###################################

def site_login(driver):

    # Code is designed for this site: https://bit.ly/labschoolscovid
    driver.get("https://")

    # Name 
    driver.find_element_by_xpath("//input[@jsname='YPqjbf']").send_keys('Your Name')

    # Email
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys('user@gmail.com')

    # Student First and Last Name
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys('First')
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys('Last')

    # Symptom Checkbox
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[14]/label/div/div[1]/div[2]").click()

    # Select Dropdown
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]").click()

    # Use Down Arrow Keys to Select 12th Option (Teacher)
    time.sleep(0.5)
    for i in range(0,12):
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
        time.sleep(0.2)
    webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()

    # Submit the Form
    # Tab to the Bottom so we can find the Submit button
    for i in range(0,16):
        time.sleep(0.3)
        webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    for i in range(0,7):
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()

    # Use the Enter Key to Submit the Form
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

    # Backup: Find the Submit Button and Click on It
    submit = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div")
    webdriver.ActionChains(driver).move_to_element(submit).click().perform()
    

###################################
driver = webdriver.Firefox()
driver.set_window_size(1200, 1500)
site_login(driver)
