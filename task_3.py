from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class Conversions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

# Test for converting Celsius to Fahrenheit temperature
    def test_1_temperature(self):
        self.driver.get('https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.html')
        self.driver.find_element_by_name("argumentConv").send_keys(10)

# Test for converting meters to feet
    def test_2_length(self):
        self.driver.get('https://www.metric-conversions.org/length/meters-to-feet.htm')
        self.driver.find_element_by_name("argumentConv").send_keys(20)

# Test for converting ounces to grams
    def test_3_weight(self):
        self.driver.get('https://www.metric-conversions.org/weight/ounces-to-grams.htm')
        self.driver.find_element_by_name("argumentConv").send_keys(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Completed!')

if __name__ == '__main__':
    unittest.main()
