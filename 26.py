from selenium import webdriver
import time
import math
# import os

link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    btn = browser.find_element_by_css_selector('button.trollface').click()
    time.sleep(2)



    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_elem = browser.find_element_by_id('input_value')
    x = math.log(math.fabs(12 * math.sin(int(x_elem.text))))
    print(x)
    browser.find_element_by_id('answer').send_keys(str(x))

    browser.find_element_by_css_selector('button.btn').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла