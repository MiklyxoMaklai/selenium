# from selenium import webdriver
# import time

# Успешный тест
# link = 'http://suninjuly.github.io/registration1.html'

# Тест падает с ошибкой NoSuchElementException
link = 'http://suninjuly.github.io/registration2.html'

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
#     input1.send_keys('Ivan')
#
#     input2 = browser.find_element_by_css_selector('div.first_block div.second_class input.second')
#     input2.send_keys('Petrov')
#
#     input3 = browser.find_element_by_css_selector('div.first_block div.third_class input.third')
#     input3.send_keys('test@step.ru')
#
#     browser.find_element_by_css_selector('form button.btn').click()
# finally:
#     # Останавливаемся на 10 секунд
#     time.sleep(10)
#
#     # закрываем браузер
#     browser.quit()
