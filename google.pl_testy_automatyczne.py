
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestGooglePl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addition(self):
        driver = self.driver
        driver.get("http://google.pl")
        search_input = driver.find_element_by_name("q")
        search_input.send_keys("2 + 3")
        search_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, "cwmcwd"))
        )
        calculator_result = driver.find_element_by_class_name("cwtlotc")
        assert "5" in calculator_result.text

    def test_subtraction(self):
        driver = self.driver
        driver.get("http://google.pl")
        search_input = driver.find_element_by_name("q")
        search_input.send_keys("5 - 2")
        search_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, "cwmcwd"))
        )
        calculator_result = driver.find_element_by_class_name("cwtlotc")
        assert "3" in calculator_result.text

    def test_multiplication(self):
        driver = self.driver
        driver.get("http://google.pl")
        search_input = driver.find_element_by_name("q")
        search_input.send_keys("2 * 3")
        search_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, "cwmcwd"))
        )
        calculator_result = driver.find_element_by_class_name("cwtlotc")
        assert "6" in calculator_result.text

    def test_division(self):
        driver = self.driver
        driver.get("http://google.pl")
        search_input = driver.find_element_by_name("q")
        search_input.send_keys("6 / 3")
        search_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.ID, "cwmcwd"))
        )
        calculator_result = driver.find_element_by_class_name("cwtlotc")
        assert "2" in calculator_result.text

    def test_search(self):
        driver = self.driver
        driver.get("http://google.pl")
        search_input = driver.find_element_by_name("q")
        search_input.send_keys("programa")
        search_input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "r"))
        )
        search_result = driver.find_element_by_class_name("r")
        assert "Programa.pl: Dedykowane systemy informatyczne oparte na chmurze" in search_result.text

    def tearDown(self):
        self.driver.close()


unittest.main()
