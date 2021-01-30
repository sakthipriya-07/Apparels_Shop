import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from customer_credentials import customer_user, customer_pwd

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
            # find Your Shopping Cart heading
            elem = driver.find_elements_by_xpath('//*[@id="content"]/h1')
            # find first item added to cart
            elem = driver.find_elements_by_xpath('//*[@id="cart-details"]/tbody/tr[1]')
            
            assert True

        except NoSuchElementException:
            self.fail("Item not added to cart")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
