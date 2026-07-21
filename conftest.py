import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from tests.config.settings import settings


@pytest.fixture(scope="function")
def driver() -> webdriver.Chrome:
    """Fixture que cria e configura o WebDriver do Chrome."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(0)  # Desabilita espera implícita (usamos apenas explícitas)

    yield driver

    driver.quit()
