from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)


    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element_by_id('book').click()

    x_elem = browser.find_element_by_id('input_value')
    x = math.log(math.fabs(12 * math.sin(int(x_elem.text))))
    print(x)
    browser.find_element_by_id('answer').send_keys(str(x))
    browser.find_element_by_id('solve').click()
    time.sleep(5)

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла