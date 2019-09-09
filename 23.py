from selenium import webdriver
import time
import math


link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)


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