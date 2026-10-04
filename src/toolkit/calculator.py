from toolkit.errors import CalculationError


def tokenize(expression: str) -> list[str]:
    """Разбивает арифмитическое выражение на токены."""
    tokens: list[str] = []
    current = ''

    index = 0

    while index < len(expression):
        char = expression[index]

        if char.isspace():
            index += 1
            continue

        if char.isdigit() or char == ".":
            current += char
            index += 1
            continue

        if char in "+-*/%()":
            if current:
                tokens.append(current)
                current = ""

            if char == "*" and index + 1 < len(expression) and expression[index + 1] == "*":
                tokens.append("**")
                index += 2
            elif char == "/" and index + 1 < len(expression) and expression[index + 1] == "/":
                tokens.append("//")
                index += 2
            else:
                tokens.append(char)
                index += 1

            continue

        raise CalculationError(f"Неизвестный символ: {char}")

    if current:
        tokens.append(current)

    return tokens

def parse_number(token: str) -> int | float:
    """Преобразуй строковый токен в целое или дробное число."""
    try:
        if '.' in token:
            return float(token)
        return int(token)
    except ValueError as error:
        raise CalculationError(f'Некоректное число: {token}') from error

def validate_tokens(tokens: list[str]) -> None:
    """Проверяет правильность последовательности токенов."""
    if not tokens:
        raise CalculationError("Пустое выражение")

    expect_operand = True
    open_parentheses = 0

    for token in tokens:
        if expect_operand:
            if token in "+-":
                continue

            if token == "(":
                open_parentheses += 1
                continue

            if token == ")":
                raise CalculationError("Неожиданная закрывающая скобка")

            parse_number(token)
            expect_operand = False

        else:
            if token in ("+", "-", "*", "/", "//", "%", "**"):
                expect_operand = True
                continue

            if token == "(":
                raise CalculationError(
                    "Ожидался оператор перед открывающей скобкой"
                )

            if token == ")":
                if open_parentheses == 0:
                    raise CalculationError("Лишняя закрывающая скобка")

                open_parentheses -= 1
                continue

            raise CalculationError(
                f"Ожидался оператор или закрывающая скобка, получен: {token}"
            )

    if expect_operand:
        raise CalculationError("Ожидался операнд в конце выражения")

    if open_parentheses != 0:
        raise CalculationError("Не хватает закрывающей скобки")

def calculate(tokens: list[str]) -> int | float:
    """Вычисляет арифметическое выражение по списку токенов."""
    values: list[int | float] = []
    operators: list[str] = []

    for index, token in enumerate(tokens):
        if token not in ("+", "-", "*", "/", "%", '//', "**", "(", ")"):
            number = parse_number(token)
            values.append(number)

            while operators and operators[-1] in ("u+", "u-"):
                apply_operator(values, operators.pop())

        elif token in "+-" and (
            index == 0 or tokens[index - 1] in ("+", "-", "*", "/", "%", '//', "**", "(")
        ):
            operators.append("u" + token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                apply_operator(values, operators.pop())

            if not operators:
                raise CalculationError("Лишняя закрывающая скобка")

            operators.pop()

            if operators and operators[-1] in ("u+", "u-"):
                apply_operator(values, operators.pop())

        else:
            while (
                    operators
                    and operators[-1] != "("
                    and operators[-1] not in ("u+", "u-")
                    and (
                            precedence(operators[-1]) > precedence(token)
                            or (
                                    precedence(operators[-1]) == precedence(token)
                                    and token != "**"
                            )
                    )
            ):
                apply_operator(values, operators.pop())

            operators.append(token)

    while operators:
        operator = operators.pop()

        if operator == "(":
            raise CalculationError("Не хватает закрывающей скобки")

        apply_operator(values, operator)

    return values[0]

def evaluate(expression: str) -> int | float:
    """Проверяет и вычисляет арифметическое выражение."""
    tokens = tokenize(expression)
    validate_tokens(tokens)
    return calculate(tokens)

def apply_operator(values: list[int | float], operator: str) -> None:
    """выполняет оператор над последними двумя значениями."""
    if operator in ('u+', 'u-'):
        value = values.pop()

        if operator == 'u-':
            value = -value

        values.append(value)
        return

    right = values.pop()
    left = values.pop()
    if operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right
    elif operator == '*':
        result = left * right
    elif operator == '/':
        if right == 0:
            raise CalculationError('Деление на ноль')
        result = left / right
    elif operator == "//":
        if right == 0:
            raise CalculationError("Деление на ноль")
        result = left // right
    elif operator == '%':
        if right == 0:
            raise CalculationError('Деление на ноль')
        result = left % right
    elif operator == "**":
        result = left ** right
    else:
        raise CalculationError(f'Неизвестный оператор: {operator}')

    values.append(result)

def precedence(operator: str) -> int:
    """Возвращает приоритет арифметического оператора"""
    if operator == "**":
        return 4
    if operator in ('u+', 'u-'):
        return 3
    if operator in ("*", "/", "//", "%"):
        return 2
    if operator in '+-':
        return 1

    raise CalculationError(f'Неизвестный оператор: {operator}')