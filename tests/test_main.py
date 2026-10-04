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