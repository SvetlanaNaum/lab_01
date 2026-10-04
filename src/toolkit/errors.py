class ToolkitError(Exception):
    """Базовая ошибка приложения."""


class CalculationError(ToolkitError):
    """Ошибка при вычислении выражения."""


class ConversionError(ToolkitError):
    """Ошибка при конвертации величин."""
