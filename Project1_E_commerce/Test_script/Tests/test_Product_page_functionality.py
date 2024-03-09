from Project1_E_commerce.Test_script.Resources.Automate_Fuctionalities.Product_page_functionality import open_menu, \
    first_item_name, product_name_list, add_to_cart_item, remove_item
from Project1_E_commerce.Test_script.Tests.Valid_functionality import login
from Project1_E_commerce.Test_script.Resources.Element_Location.Product_List_page import Side_menu
# Open Menu
def test_TP_1():
    try:
        driver=login()
        driver,Text=open_menu(driver=driver)
        assert Text == "All Items"
    finally:
        driver.quit()

def test_TP_2():
    try:
        driver=login()
        list_of_item,driver= product_name_list(driver=driver)
        item=list_of_item[0]
        driver = add_to_cart_item(item_name=item, driver=driver)
        driver,Text=open_menu(driver=driver)
        assert Text == "All Items"
    finally:
        driver.quit()

def test_TP_3():
    try:
        driver=login()
        list_of_item,driver= product_name_list(driver=driver)
        for item in list_of_item:
            driver = add_to_cart_item(item_name=item, driver=driver)
        driver,Text=open_menu(driver=driver)
        assert Text == "All Items"
    finally:
        driver.quit()

def test_TP_4():
    try:
        driver = login()
        list_of_item, driver = product_name_list(driver=driver)
        item = list_of_item[0]
        driver = add_to_cart_item(item_name=item, driver=driver)
        driver=remove_item(driver=driver,item=item)
        driver, Text = open_menu(driver=driver)
        assert Text == "All Items"
    finally:
        driver.quit()


def test_TP_5():
    try:
        driver=login()
        list_of_item,driver= product_name_list(driver=driver)
        for i in [1,4,3,5]:
            item=list_of_item[i]
            driver = add_to_cart_item(item_name=item, driver=driver)
        for i in [4,5]:
            item=list_of_item[i]
            driver = remove_item(driver=driver, item=item)
        driver,Text=open_menu(driver=driver)
        assert Text == "All Items"
    finally:
        driver.quit()




