import pytest

from toolkit.calculator import evaluate
from toolkit.errors import CalculationError


def test_addition() -> None:
    """Проверяет сложение"""
    assert evaluate('2 + 3') == 5

def test_operations_precedence() -> None:
    """Проверяет приоритет умножения."""
    assert evaluate('2 + 3 * 4') == 14

def test_parentheses() -> None:
    """Проверяет вычисление выражения со скобками."""
    assert evaluate('(2 + 3) * 4') == 20

def test_division() -> None:
    """Проверяте деление."""
    assert evaluate('10 / 2') == 5

def test_power() -> None:
    """Проверяет возведение в степень."""
    assert evaluate('2 ** 3') == 8

def test_power_precedence() -> None:
    """Проверяет приоритет возведения в степень."""
    assert evaluate('2 + 3 ** 2') == 11

def test_power_right_associative() -> None:
    """Проверяет вычисление степени справа налево."""
    assert evaluate('2 ** 3 ** 2') == 512

def test_unar_operator() -> None:
    """Проверяет унарный минус."""
    assert evaluate('2 * -3') == -6

def test_division_zero() -> None:
    """Проверяет ошибку при делении на ноль."""
    with pytest.raises(CalculationError):
        evaluate('10 / 0')

def test_empty_expression() -> None:
    """Проверяет ошибку для пустого выражения."""
    with pytest.raises(CalculationError):
        evaluate("")

def test_integer_division() -> None:
    """Проверяет целочисленное деление."""
    assert evaluate("7 // 2") == 3

def test_modulo() -> None:
    """Проверяет остаток от деления."""
    assert evaluate("10 % 3") == 1

def test_unknown_character() -> None:
    """Проверяет ошибку при неизвестном символе."""
    with pytest.raises(CalculationError):
        evaluate("2 & 3")

def test_two_operators_in_a_row() -> None:
    """Проверяет ошибку при двух операторах подряд."""
    with pytest.raises(CalculationError):
        evaluate("2 + * 3")

def test_invalid_number() -> None:
    """Проверяет ошибку при некорректном числе."""
    with pytest.raises(CalculationError):
        evaluate("2.3.4 + 1")