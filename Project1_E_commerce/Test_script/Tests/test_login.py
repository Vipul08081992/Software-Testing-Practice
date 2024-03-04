import pytest
from Project1_E_commerce.Test_script.Resources.Automate_Fuctionalities.Login_functionality import open_Url \
    , input_credentials, login_button_click
from Project1_E_commerce.Test_script.Resources.Element_Location.URLs_of_Website import product_page_url
from Project1_E_commerce.Test_script.Read_Data.Read_login_credentials import read_data_of_row


#Test: Verify login functionality
@pytest.mark.parametrize("test_cred",read_data_of_row("D:\\Software-Testing-Practice\\Project1_E_commerce\\Test_Cases\\Swag Labs.xlsx",6,7,11,17))
def test_login_chrome(test_cred):
    try:
        driver=open_Url()
        username=test_cred["username"]
        password=test_cred["password"]
        driver=input_credentials(driver=driver, username=username, password=password)
        url,driver=login_button_click(driver=driver)
        assert url == product_page_url() , "Unable to Login"
    finally:
        driver.quit()