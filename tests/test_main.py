import subprocess
import sys


def test_calculate_cli() -> None:
    """Проверяет вычисление выражения через командную строку."""
    result = subprocess.run(
        [
            sys.executable,
            "src/main.py",
            "calculate",
            "2 + 3 * 4",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == "14"


def test_convert_cli() -> None:
    """Проверяет конвертацию через командную строку."""
    result = subprocess.run(
        [
            sys.executable,
            "src/main.py",
            "convert",
            "10",
            "cm",
            "m",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == "0.1"

def test_calculate_error_returns_code_2() -> None:
    """Проверяет код ошибки калькулятора."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "calc",
            "10 / 0",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "Деление на ноль" in result.stderr
    assert result.stdout == ""


def test_convert_error_returns_code_2() -> None:
    """Проверяет код ошибки конвертера."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "convert",
            "100",
            "--from",
            "cm",
            "--to",
            "kg",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "Несовместимые единицы" in result.stderr
    assert result.stdout == ""