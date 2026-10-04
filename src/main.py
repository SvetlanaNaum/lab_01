import argparse

from toolkit.calculator import evaluate
from toolkit.converter import convert
from toolkit.errors import CalculationError, ConversionError


def main() -> None:
    """Запускает командный интерфейс программы"""
    parser = argparse.ArgumentParser(
        description='Калькулятор и конвертер величин.'
    )

    subparsers = parser.add_subparsers(dest='command')

    calculate_parser = subparsers.add_parser(
        'calculate',
        help='Вычислить арифмитическое выражение.',
    )
    calculate_parser.add_argument(
        'expression',
        help='Арифмитическое выражение',
    )

    convert_parser = subparsers.add_parser(
        'convert',
        help='Конвертировать величину.',
    )
    convert_parser.add_argument(
        'value',
        type=float,
        help='Значение.',
    )
    convert_parser.add_argument(
        'from_unit',
        help='Исходная единица.'
    )
    convert_parser.add_argument(
        'to_unit',
        help='целевая единица.'
    )

    args = parser.parse_args()

    if args.command == 'calculate':
        try:
            result = evaluate(args.expression)
            print(result)
        except CalculationError as error:
            print(f'Ошибка: {error}')

    elif args.command == "convert":
        try:
            result = convert(args.value, args.from_unit, args.to_unit)
            print(result)
        except ConversionError as error:
            print(f'Ошибка: {error}')

if __name__ == '__main__':
    main()