from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_present(browser):
    wait = WebDriverWait(browser, 10)
    browser.get(url)
    try:
        add_to_cart_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket'))
        )
    except TimeoutException:
        add_to_cart_button = None

    assert add_to_cart_button, "That button doesn't exist"
