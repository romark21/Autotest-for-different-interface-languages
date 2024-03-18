from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Input language!')


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    service = Service(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    yield driver

    sleep(10)  # По заданию значение должно быть 30, но я установил меньше, чтоб не тратить ваше время.
    driver.quit()
