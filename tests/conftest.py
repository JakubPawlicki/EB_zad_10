import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = ChromeService(ChromeDriverManager().install()
    service = ChromeService(ChromeDriverManager().install(), options=options)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.get("https://victorious-moss-09004da03.5.azurestaticapps.net/")
    yield driver
    driver.quit()
