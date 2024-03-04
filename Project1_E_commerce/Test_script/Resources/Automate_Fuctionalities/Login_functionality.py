from selenium import webdriver

from Project1_E_commerce.Test_script.Resources.Element_Location.Login_page import passsword_id, username_id, submit_id
from Project1_E_commerce.Test_script.Resources.Element_Location.Product_List_page import Product_Page
from Project1_E_commerce.Test_script.Resources.Element_Location.URLs_of_Website import login_page_url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#Open Login page Url:
def open_Url():
    driver = webdriver.Chrome()
    driver.get(login_page_url())
    driver.maximize_window()
    return driver

#Input credentials
def input_credentials(driver,username,password):
    try:
        driver.find_element(By.ID,username_id()).send_keys(username)
        driver.find_element(By.ID,passsword_id()).send_keys(password)
        return driver
    except ValueError:
        print("Element Not Found")

#Click on Login button
def login_button_click(driver):
    try:
        driver.find_element(By.ID,submit_id()).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,Product_Page.sort_button_xpath())))
        url= driver.current_url
        return url,driver
    except ValueError:
        print("Element Not Found")







