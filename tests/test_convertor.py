import pytest

from toolkit.converter import convert
from toolkit.errors import ConversionError


def test_length_conversion() -> None:
    """Проверяет перевод сантиметров в метры."""
    assert convert(100, "cm", "m") == 1


def test_mass_conversion() -> None:
    """Проверяет перевод килограммов в граммы."""
    assert convert(2, "kg", "g") == 2000


def test_temperature_conversion() -> None:
    """Проверяет перевод градусов Цельсия в Фаренгейты."""
    assert convert(100, "c", "f") == 212


def test_units_are_case_insensitive() -> None:
    """Проверяет, что регистр единиц не имеет значения."""
    assert convert(1, "KM", "M") == 1000


def test_unknown_unit() -> None:
    """Проверяет ошибку при неизвестной единице."""
    with pytest.raises(ConversionError):
        convert(10, "abc", "m")
