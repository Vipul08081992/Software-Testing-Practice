from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.resourses.Element_Location.Product_List_page import Product_Page,Side_menu
from tests.Helper.Automate_Fuctionalities.Login_functionality import  login_button_click
from tests.Helper.Generic_functions.Read_Data import read_data_of_cell
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


#1.When no Product Added
def filter_button():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    driver=login_button_click(username=username, password=password)
    try:
        element=driver.find_element(By.CLASS_NAME,Product_Page.filter_button_class())
        dropdown=Select(element)
        return dropdown
    except ValueError:
        print("Element Not Found")

#Get option in dropdown
def options_in_dropdown():
    dropdown=filter_button()
    list_of_dropdown=dropdown.options
    return list_of_dropdown

#Count number of options
def count_options():
    return len(options_in_dropdown())

#Select options
def select_option(value):
    dropdown=filter_button()
    element=dropdown.select_by_visible_text(value)
    return element







#2.Product are added
def menu_button_product_add():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
    try:
        for i in (1,4):
            items_to_add[i].click()
        pro_page.find_element(By.ID,Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#3.Add all the products availlable
def menu_button_product_all_add():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in range(len(items_to_add)):
            items_to_add[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#4.Remove some of added products
def menu_button_product_add_remove_some():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in (1,3,4,2):
            items_to_add[i].click()
        items_to_remove=pro_page.find_elements(By.XPATH,Product_Page.remove_from_cart_button_xpath())
        for i in (1,3):
            items_to_remove[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#5.Remove all selected items selected
def menu_button_product_add_remove_all():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in (1, 3, 4, 2):
            items_to_add[i].click()
        items_to_remove = pro_page.find_elements(By.XPATH, Product_Page.remove_from_cart_button_xpath())
        for i in range(len(items_to_remove)):
            items_to_remove[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
        print("Element Not Found")

#6.Add all products available and then remove them all
def menu_button_product_add_all_remove_all():
    username = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 2)
    password = read_data_of_cell(
        '/src/resources/Data/Valid Credentials.xlsx', 2, 3)
    pro_page = login_account_chrome(username=username, password=password)
    try:
        items_to_add = pro_page.find_elements(By.XPATH, Product_Page.add_to_cart_button_xpath())
        for i in range(len(items_to_add)):
            items_to_add[i].click()
        items_to_remove = pro_page.find_elements(By.XPATH, Product_Page.remove_from_cart_button_xpath())
        for i in range(len(items_to_remove)):
            items_to_remove[i].click()
        pro_page.find_element(By.ID, Product_Page.menu_button_id()).click()
        time.sleep(5)
        return pro_page.find_element(By.ID,Side_menu.all_item_id()).is_displayed()
    except ValueError:
            print("Element Not Found")


