import argparse

from toolkit.calculator import evaluate
from toolkit.converter import convert
from toolkit.errors import CalculationError, ConversionError


def main() -> None:
    """Запускает командный интерфейс программы."""
    parser = argparse.ArgumentParser(
        description="Калькулятор и конвертер величин.",
    )

    subparsers = parser.add_subparsers(dest="command")

    calc_parser = subparsers.add_parser(
        "calc",
        help="Вычислить арифметическое выражение.",
    )
    calc_parser.add_argument(
        "expression",
        help="Арифметическое выражение.",
    )

    convert_parser = subparsers.add_parser(
        "convert",
        help="Конвертировать величину.",
    )
    convert_parser.add_argument(
        "value",
        type=float,
        help="Значение.",
    )
    convert_parser.add_argument(
        "--from",
        dest="from_unit",
        required=True,
        help="Исходная единица.",
    )
    convert_parser.add_argument(
        "--to",
        dest="to_unit",
        required=True,
        help="Целевая единица.",
    )

    args = parser.parse_args()

    if args.command == "calc":
        try:
            result = evaluate(args.expression)
            print(result)
        except CalculationError as error:
            print(f"Ошибка: {error}")

    elif args.command == "convert":
        try:
            result = convert(
                args.value,
                args.from_unit,
                args.to_unit,
            )
            print(result)
        except ConversionError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()