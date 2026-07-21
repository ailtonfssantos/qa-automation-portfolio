from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.locators.login_locators import LoginLocators


class LoginPage:
    """Page Object para a página de login do SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """Inicializa a página com o driver do Selenium."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Abre a página de login."""
        self.driver.get("https://www.saucedemo.com")

    def enter_username(self, username: str) -> None:
        """Digita o nome de usuário no campo."""
        username_field = self.wait.until(
            EC.presence_of_element_located(LoginLocators.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """Digita a senha no campo."""
        password_field = self.wait.until(
            EC.presence_of_element_located(LoginLocators.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self) -> None:
        """Clica no botão de login."""
        login_button = self.wait.until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
        )
        login_button.click()

    def login(self, username: str, password: str) -> None:
        """Realiza o login completo."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self) -> str:
        """Retorna a mensagem de erro exibida."""
        error_element = self.wait.until(
            EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE)
        )
        return str(error_element.text)
