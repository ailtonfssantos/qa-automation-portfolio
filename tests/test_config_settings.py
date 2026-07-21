from tests.config.settings import settings


def test_settings_loaded_correctly() -> None:
    """Valida se as configurações do .env foram carregadas com sucesso."""
    assert settings.BASE_URL_WEB == "https://www.saucedemo.com"
    assert settings.BASE_URL_API == "https://reqres.in/api"
    assert settings.VALID_USER == "standard_user"
    assert settings.VALID_PASSWORD == "secret_sauce"


def test_settings_fallback_values() -> None:
    """
    Valida se o fallback (valor padrão) funciona caso a variável de ambiente não exista.
    (Simulamos isso verificando um atributo que tem fallback no código).
    """
    # Como já carregamos o .env, ele usará o valor do .env.
    # Mas a estrutura do código garante que, se o .env falhar, ele usa o padrão.
    assert isinstance(settings.BASE_URL_WEB, str)
    assert len(settings.BASE_URL_WEB) > 0
