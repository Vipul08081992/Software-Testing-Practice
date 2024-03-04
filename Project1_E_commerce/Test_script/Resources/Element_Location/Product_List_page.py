
class Product_Page:

    #Product Heading
    @staticmethod
    def heading_prodouct():
        return '//span[contains(text(),"Products")]'

    #Cart Symbol
    @staticmethod
    def cart_symbol_class():
        return "shopping_cart_link"

    #Menu button
    @staticmethod
    def menu_button_id():
        return "react-burger-menu-btn"

    #Sort button
    @staticmethod
    def sort_button_xpath():
        return "//select[@class='product_sort_container']"
    #List of Items name
    @staticmethod
    def list_item_xpath():
        return "//div[@class='inventory_item_name ']"

    #List of Item price
    @staticmethod
    def item_price_xpath():
        return "//div[@class='inventory_item_price']"
    #First Item:
    @staticmethod
    def first_item_xpath():
        return "//div[@class='inventory_item_name '][1]"

    # Add to cart button any
    @staticmethod
    def add_to_cart_button_xpath():
        return "//button[contains(text(),'Add to cart')]"

    #Remove Item from cart
    @staticmethod
    def remove_from_cart_button_xpath():
        return "//button[contains(text(),'Remove')]"

    #Item details

    def item_details_xpath(self,item):
        item_details= f"//img[@alt='{item}']"
        return item_details
    #Count shown in symbol
    @staticmethod
    def value_symbol_xpath():
        return "//span[@class='shopping_cart_badge']"

class Side_menu:
        # Cross button
    @staticmethod
    def cross_button_id():
        return "react-burger-cross-btn"

    #All Item
    @staticmethod
    def all_item_id():
        return "inventory_sidebar_link"

    #About
    @staticmethod
    def about_id():
        return "about_sidebar_link"

    #Logout
    @staticmethod
    def logout_id():
        return "logout_sidebar_link"

    #Reset App State
    @staticmethod
    def reset_app_state_id():
        return "reset_sidebar_link"

class Filter:
    #Name (A to Z) option
    @staticmethod
    def name_AtoZ_css():
        return "option[value*='az']"

    #Name (Z to A) option
    @staticmethod
    def name_ZtoA_css():
        return "option[value*='za']"

    #Price (low to high)option
    @staticmethod
    def price_ltoh_css():
        return "option[value*='lohi']"

    # Price (high to low)option
    @staticmethod
    def price_htot_css():
        return "option[value*='hilo']"


