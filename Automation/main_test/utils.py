import random
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests, os, logging, time
from selenium import webdriver

import logging



@contextmanager
def services_context_wrapper(screenshot=None):
    global driver
    try:
        testcase_id = screenshot.split(".")
        logging.info(f"Start for {testcase_id[0]}")
        c = Options()
        # c.add_argument("--headless=new")
        c.add_argument("--window-size=1920,1080")
        # c.add_argument("--no-sandbox")
        # # c.add_argument("enable-automation")
        # c.add_argument("--disable-blink-features=AutomationControlled")
        # c.add_argument("--disable-dev-shm-usage")
        # prefs={"download.default_directory":os.getcwd()+"/downloads"}
        # c.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(options=c)
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=c)
        # driver = webdriver.Remote(command_executor='http://selenium__standalone-chrome:4444/wd/hub',options=c)
        # driver = webdriver.Chrome()
        yield driver
    except Exception:
        logging.info(f"End for {testcase_id[0]}")
        if screenshot:
            driver.save_screenshot(screenshot)
        raise
    finally:
        logging.info(f"End for {testcase_id[0]}")
        logging.info(os.getcwd())
        driver.quit()



def Start_Driver(driver_name):
    if driver_name == "Chrome":
        return webdriver.Chrome()


def LOGIN(driver):
    # Login
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
