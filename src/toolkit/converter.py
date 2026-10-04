from toolkit.constants import LENGTH_TO_METER, MASS_TO_KILOGRAM
from toolkit.errors import ConversionError


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Переводит значение длины из одной единицы в другую."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in LENGTH_TO_METER:
        raise ConversionError(f"Неизвестная единица длины: {from_unit}")

    if to_unit not in LENGTH_TO_METER:
        raise ConversionError(f"Неизвестная единица длины: {to_unit}")

    value_in_meter = value * LENGTH_TO_METER[from_unit]
    result = value_in_meter / LENGTH_TO_METER[to_unit]

    return result


def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in MASS_TO_KILOGRAM:
        raise ConversionError(f"Неизвестная единица массы: {from_unit}")

    if to_unit not in MASS_TO_KILOGRAM:
        raise ConversionError(f"Нетзвестная единица массы: {to_unit}")

    value_in_kilogram = value * MASS_TO_KILOGRAM[from_unit]
    result = value_in_kilogram / MASS_TO_KILOGRAM[to_unit]

    return result


def convert_temperature(
    value: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """Переводит температуру между C, F, K."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in ("c", "f", "k"):
        raise ConversionError(f"Неизвестная единица температуры: {from_unit}")

    if to_unit not in ("c", "f", "k"):
        raise ConversionError(f"Неизвестная единица температуры: {to_unit}")

    if from_unit == "c" and value < -273.15:
        raise ConversionError("Температура ниже абсолютного нуля")

    if from_unit == "f" and value < -459.67:
        raise ConversionError("Температура ниже абсолютного нуля")

    if from_unit == "k" and value < 0:
        raise ConversionError("Температура ниже абсолютного нуля")

    if from_unit == to_unit:
        return value

    if from_unit == "c":
        if to_unit == "f":
            return value * 9 / 5 + 32
        return value + 273.15

    if from_unit == "f":
        if to_unit == "c":
            return (value - 32) * 5 / 9
        return (value - 32) * 5 / 9 + 273.15

    if to_unit == "c":
        return value - 273.15

    return (value - 273.15) * 9 / 5 + 32


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Конвертирует значение между поддерживаемыми функциями"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit in LENGTH_TO_METER and to_unit in LENGTH_TO_METER:
        return convert_length(value, from_unit, to_unit)

    if from_unit in MASS_TO_KILOGRAM and to_unit in MASS_TO_KILOGRAM:
        return convert_mass(value, from_unit, to_unit)

    if from_unit in ("c", "f", "k") and to_unit in ("c", "f", "k"):
        return convert_temperature(value, from_unit, to_unit)

    raise ConversionError(f"Несовместимые единицы: {from_unit} и {to_unit}")
