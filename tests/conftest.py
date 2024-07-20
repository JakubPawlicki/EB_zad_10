import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    chrome_options.binary_location = "/opt/hostedtoolcache/setup-chrome/chromium/1330686/x64"
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get("https://victorious-moss-09004da03.5.azurestaticapps.net/")
    yield driver
    driver.quit()
