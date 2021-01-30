import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from customer_credentials import customer_user, customer_pwd, cust_first_name, cust_last_name, cust_email, cust_address, cust_postal, cust_city

class Store_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_store(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://sakthipriyasenthilkumar.pythonanywhere.com")
        elem = driver.find_element_by_xpath("/html/body/nav/ul[2]/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(customer_user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(customer_pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Logged in"

        try:
            # click on first product
            elem = driver.find_element_by_xpath('//*[@id="main"]/div[1]/a[1]').click()
            time.sleep(2)
            # click add to cart
            elem = driver.find_element_by_xpath('//*[@id="content"]/div/form/input[3]').click()
            time.sleep(2)
            # click checkout button
            elem = driver.find_element_by_xpath('//*[@id="content"]/p/a[2]').click()      
            time.sleep(2)    
            assert "Added to cart"

            elem = driver.find_element_by_id("id_first_name")
            elem.send_keys(cust_first_name)
            elem = driver.find_element_by_id("id_last_name")
            elem.send_keys(cust_last_name)
            elem = driver.find_element_by_id("id_email")
            elem.send_keys(cust_email)
            elem = driver.find_element_by_id("id_address")
            elem.send_keys(cust_address)
            elem = driver.find_element_by_id("id_postal_code")
            elem.send_keys(cust_postal)
            elem = driver.find_element_by_id("id_city")
            elem.send_keys(cust_city)
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="content"]/form/p[7]/input').click()
            time.sleep(2)
            assert "Shipping details entered"

            ########## NEEDS TO BE UPDATED FOR PURCHASE CHECKOUT ###########

        except NoSuchElementException:
            self.fail("Item not added to cart")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
