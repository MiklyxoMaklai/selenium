import unittest
from selenium import webdriver

class TestRegister(unittest.TestCase):
    def test_reg1_test(self):
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/registration1.html'
        browser.get(link)

        input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input1.send_keys('Ivan')

        input2 = browser.find_element_by_css_selector('div.first_block div.second_class input.second')
        input2.send_keys('Petrov')

        input3 = browser.find_element_by_css_selector('div.first_block div.third_class input.third')
        input3.send_keys('test@step.ru')

        browser.find_element_by_css_selector('form button.btn').click()

        self.assertEqual(browser.find_element_by_css_selector('h1').text, 'Congratulations! You have successfully registered!', 'Should be absolute value of a number')
        browser.quit()


    def test_reg2(self):
        browser = webdriver.Chrome()
        link = 'http://suninjuly.github.io/registration2.html'
        browser.get(link)

        input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input1.send_keys('Ivan')

        input2 = browser.find_element_by_css_selector('div.first_block div.second_class input.second')
        input2.send_keys('Petrov')

        input3 = browser.find_element_by_css_selector('div.first_block div.third_class input.third')
        input3.send_keys('test@step.ru')

        browser.find_element_by_css_selector('form button.btn').click()
        self.assertEqual(browser.find_element_by_css_selector('h1').text, 'Congratulations! You have successfully registered!', 'Should be absolute value of a number')
        browser.quit()