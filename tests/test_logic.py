from app.core.logic import dodaj_liczby


def test_dodaj_liczby():
    assert dodaj_liczby(2, 3) == 5
    assert dodaj_liczby(-1, 1) == 0
