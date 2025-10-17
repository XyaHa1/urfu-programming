import pytest

from ..core import Title


@pytest.mark.parametrize(
    "note, expected",
    [
        ("python", "Python"),
        ("  pePSi  - cola   vaNILLa ", "Pepsi-cola Vanilla"),
        ("   пельмЕНи униВЕрсальные  ", "Пельмени Универсальные"),
        ("   ПЕЛьменИ     ЦЕзарь     -Классические", "Пельмени Цезарь-классические"),
        ("   Лук ЯЛТИНСкий", "Лук Ялтинский"),
        ("  лук- Порей ", "Лук-порей"),
        ("  ЛУК -Порей ", "Лук-порей"),
        ("Картофель", "Картофель"),
        ("fresh", "Fresh"),
        ("   fries   ", "Fries"),
        ("  ИВАН -     Чай", "Иван-чай"),
    ],
)
def test_title_format(note, expected):
    assert Title(note).title == expected
