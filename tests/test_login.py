import pytest
from tests.pages.login_page import LoginPage
from tests.config.settings import settings


@pytest.mark.smoke
def test_valid_login(driver: pytest.FixtureRequest) -> None:
    """Testa login com credenciais válidas."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(settings.VALID_USER, settings.VALID_PASSWORD)

    # Valida que foi redirecionado para a página de produtos
    assert "inventory.html" in driver.current_url


@pytest.mark.regression
def test_invalid_login(driver: pytest.FixtureRequest) -> None:
    """Testa login com credenciais inválidas."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    # Valida que a mensagem de erro é exibida
    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message
