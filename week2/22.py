from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element_by_id('num1')
    x1 = int(num1.text)

    num2 = browser.find_element_by_id('num2')
    x2 = int(num2.text)

    summ = x1 + x2
    print('summa', summ)

    browser.find_element_by_css_selector('#dropdown').click()
    browser.find_element_by_css_selector('#dropdown [value="' + str(summ) + '"]').click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла