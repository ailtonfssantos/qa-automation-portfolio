def soma(a: int, b: int) -> int:
    """Soma dois números inteiros e retorna o resultado."""
    return a + b


def test_soma() -> None:
    """Testa a função de soma com valores inteiros."""
    resultado: int = soma(10, 5)
    assert resultado == 15
