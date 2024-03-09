from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Project1_E_commerce.Test_script.Resources.Element_Location.Product_Detail_page import item_name_xpath, \
    back_to_product_button_name
from selenium.webdriver.support.ui import Select
from Project1_E_commerce.Test_script.Resources.Element_Location.Product_List_page import Product_Page,Side_menu
from Project1_E_commerce.Test_script.Tests.Valid_functionality import login
from Uitils.format_the_string import format_string_low_replace

#Open Menu:
def open_menu(driver):
    driver.find_element(By.ID,Product_Page.menu_button_id()).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID,Side_menu.all_item_id())))
    Text=driver.find_element(By.ID,Side_menu.all_item_id()).text
    return driver,Text

#Heading of Product page:
def heading_product_page(driver):
  heading= driver.find_element(By.XPATH,Product_Page.heading_prodouct()).text()
  return heading

# List of Products name:
def product_name_list(driver):
    product_names=[]
    list_products_ele=driver.find_elements(By.XPATH,Product_Page.list_item_xpath())
    for i in list_products_ele:
        product_names.append(i.text)
    return product_names,driver

#List of Product price:
def product_price_list(driver):
    list_product_price=[]
    list_product_value=driver.find_elements(By.XPATH,Product_Page.item_price_xpath())
    for p in list_product_value:
        price=p.text
        list_product_price.append(float(price[1:]))
    return list_product_price

#Sort the Product List:
def sort_product_list(driver,value):
    dropdown=Select(driver.find_element(By.XPATH,Product_Page.sort_button_xpath()))
    if value == "Name (A to Z)":
        dropdown.select_by_visible_text("Name (A to Z)")
        return driver
    elif value == "Name (Z to A)":
        dropdown.select_by_visible_text("Name (Z to A)")
        return driver
    elif value == "Price (low to high)":
        dropdown.select_by_visible_text("Price (low to high)")
        return driver
    elif value == "Price (high to low)":
        dropdown.select_by_visible_text("Price (high to low)")
        return driver
    else:
        return "Sorting not in list"

#Get Name of First Item:
def first_item_name(driver):
    item_name=driver.find_element(By.XPATH,Product_Page.first_item_xpath()).text
    return item_name

#Add items to cart:
## Make xpath of the Add to cart button
def xpath_of_cart_button(item):
    item_change=format_string_low_replace(item)
    item_cart= "add-to-cart-" + item_change
    item_list_xpath=f"//button[@id='{item_cart}']"
    return item_list_xpath
## Add item to cart
def add_to_cart_item(item_name,driver):
    item_xpath= xpath_of_cart_button(item_name)
    driver.find_element(By.XPATH,item_xpath).click()
    return driver

# Remove item from cart:
##Make xpath of the remove item
def xpath_of_remove_button(item):
    item_change=format_string_low_replace(item)
    item_list_xpath=f"//button[@id='remove-{item_change}']"
    return item_list_xpath
##Remove item from cart
def remove_item(driver,item):
    driver.find_element(By.XPATH,xpath_of_remove_button(item)).click()
    return driver

#Opening cart page
def open_cart_page(driver):
    driver.find_element(By.CLASS_NAME, Product_Page.cart_symbol_class()).click()
    return driver

#Count value of items in cart
def count_item_add_to_cart(driver):
    item=driver.find_elements(By.XPATH,"//button[contains(text(),'Remove')]")
    count=len(item)
    return driver,count

#Count of items not selected
def count_item_not_add_to_cart(driver):
    item=driver.find_elements(By.XPATH,"//button[contains(text(),'Add to cart')]")
    count=len(item)
    return driver,count

#Value shown in cart icon
def items_show_in_cart_icon(driver):
    value_on_cart=int(driver.find_element(By.XPATH,Product_Page.value_symbol_xpath()).text())
    return value_on_cart,driver

#Open Sorting button
def sorting_dropdown(driver):
    driver.find_element(By.XPATH,Product_Page.sort_button_xpath()).click()
    return driver

#Specific Item detail page open
def open_sepecfic_item_detail(driver,item_text):
    item_detail_xpath= Product_Page.item_details_xpath(item_text)
    driver.find_element(By.XPATH,item_detail_xpath).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,item_name_xpath())))
    Name=driver.find_element(By.XPATH,back_to_product_button_name()).text()
    return driver,Name
#


