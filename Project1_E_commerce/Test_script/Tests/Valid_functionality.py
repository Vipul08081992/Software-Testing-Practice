# Login
from Project1_E_commerce.Test_script.Resources.Automate_Fuctionalities.Login_functionality import open_Url, \
    input_credentials, login_button_click
from Project1_E_commerce.Test_script.Resources.Valid_Data import username,password

def login():
        driver=open_Url()
        driver=input_credentials(driver=driver, username=username(), password=password())
        url,driver=login_button_click(driver)
        return driver

