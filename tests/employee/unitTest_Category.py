import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from employee_credentials import employee_pwd, employee_user


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
        elem.send_keys(employee_user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(employee_pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Logged in"

        try:
            # click on '+ Add' on Catagories card
            elem = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div/div[1]/div/div[2]/a[1]').click()
            time.sleep(2)
            elem = driver.find_element_by_id("id_name")
            elem.send_keys("New Category")
            elem = driver.find_element_by_id("id_slug")
            elem.send_keys("test-slug")
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="content"]/form/div/button').click()
            time.sleep(2)
            elem = driver.find_elements_by_link_text('New Category')[0].click()
            time.sleep(2)
            assert "New item created"

            elem = driver.find_element_by_id("id_name")
            elem.send_keys(" update")
            elem = driver.find_element_by_xpath('//*[@id="content"]/form/div/button').click()
            time.sleep(2)
            elem = driver.find_elements_by_link_text('New Category update')[0].click()
            time.sleep(2)
            assert "New item updated"

            elem = driver.find_element_by_xpath('//*[@id="content"]/form/div/a').click()
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="content"]/form/div/input').click()
            time.sleep(2)
            elem = driver.find_elements_by_link_text('New Category update')
            assert len(elem) == 0
            assert "New item deleted"

        except NoSuchElementException:
            self.fail("Item tests failed")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
