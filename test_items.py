from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def test_page(browser, language):
    # given
    print(f'Using language {language}')
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    # when
    browser.get(url)

    # then
    WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn"))
    )
