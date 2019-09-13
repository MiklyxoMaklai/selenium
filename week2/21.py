from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)


    treasure = browser.find_element_by_id('treasure')
    x = treasure.get_attribute('valuex')

    inputAns = browser.find_element_by_id('answer')
    inputAns.send_keys(calc(x))

    check = browser.find_element_by_id('robotCheckbox')
    check.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла