import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()

@pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, link):
    link = f'https://stepik.org/lesson/{link}/step/1'
    browser.get(link)
    answer = str(math.log(int(time.time())))
    time.sleep(2)
    print('answer--> ', answer)

    browser.find_element_by_css_selector('textarea[id^="ember"]').send_keys(answer)
    time.sleep(1)
    browser.find_element_by_css_selector('button.submit-submission').click()
    time.sleep(2)
    assert browser.find_element_by_css_selector('pre.smart-hints__hint').text == 'Correct!', print('FALSE -->', browser.find_element_by_css_selector('pre.smart-hints__hint').text)
    print(browser.find_element_by_css_selector('pre.smart-hints__hint').text)

