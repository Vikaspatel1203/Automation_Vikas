import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from main_test import Report_Mail
from main_test import utils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
import os

# ---------- XPATH'S --------------
LOGIN_BUTTON = '//a[text()="Login"]'
SEARCH_BAR = '//input[@name="q"]'
CROSS_ICON = '//button[text()="✕"]'


def test_github():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://github.com/login")
    driver.find_element(By.ID, 'login_field').send_keys('1079maan')
    driver.find_element(By.ID, 'password').send_keys('maan2728')
    driver.find_element(By.NAME, 'commit').click()
    time.sleep(3)
    driver.quit()


def test_github_data():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://github.com/login")
    driver.find_element(By.ID, 'login_field').send_keys('1079maan')
    driver.find_element(By.ID, 'password').send_keys('maan2728')
    driver.find_element(By.NAME, 'commit').click()
    time.sleep(3)
    driver.quit()


def test_case_01():
    with utils.services_context_wrapper("test_case_1.png") as driver:
        driver.maximize_window()
        utils.LOGIN(driver)
        driver.implicitly_wait(10)
        act_title = driver.find_element(
            By.XPATH, LOGIN_BUTTON
        ).text
        assert act_title == "Login"
        logging.info("Login is successful.")
        rt_value = driver.find_element(
            By.XPATH, LOGIN_BUTTON
        ).is_displayed()
        assert rt_value
        # click at crossbar
        (WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, CROSS_ICON))).click())
        # Search the product in search bar and click the Enter
        (WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR))).send_keys("iphone",
                                                                                                           Keys.ENTER))
        # Result
        result = driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')
        logging.info(len(result))
        assert len(result) >= 1
        logging.info("We have got the more then one results")
        Report_Mail.Success_List_Append("TC_01", "Open flipkart and search the product", "Pass")


def test_case_02():
    with utils.services_context_wrapper("test_case_2.png") as driver:
        driver.maximize_window()
        utils.LOGIN(driver)
        driver.implicitly_wait(10)
        act_title = driver.find_element(
            By.XPATH, LOGIN_BUTTON
        ).text
        assert act_title == "gin"
        logging.info("Login is successful.")
        rt_value = driver.find_element(
            By.XPATH, LOGIN_BUTTON
        ).is_displayed()
        assert rt_value
        # click at crossbar
        (WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[tex()="X"]'))).click())
        # Search the product in search bar and click the Enter
        (WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR))).send_keys("iphone",
                                                                                                           Keys.ENTER))
        # Result
        result = driver.find_elements(By.XPATH, '//div[@class="_4rR01T"]')
        logging.info(len(result))
        assert len(result) >= 1
        logging.info("We have got the more then one results")
        Report_Mail.Success_List_Append("TC_02", "Open flipkart and search the product", "Pass")

