import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env na raiz do projeto
load_dotenv()


class Settings:
    """Classe centralizada para gerenciar configurações do ambiente de teste."""

    BASE_URL_WEB: str = os.getenv("BASE_URL_WEB", "https://www.saucedemo.com")
    BASE_URL_API: str = os.getenv("BASE_URL_API", "https://reqres.in/api")
    VALID_USER: str = os.getenv("VALID_USER", "standard_user")
    VALID_PASSWORD: str = os.getenv("VALID_PASSWORD", "secret_sauce")


# Instância global para ser importada facilmente
settings = Settings()
