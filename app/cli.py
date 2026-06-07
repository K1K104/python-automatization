from app.core.logic import dodaj_liczby


def main():
    print("Uruchamianie programu...")
    wynik = dodaj_liczby(5, 7)
    print(f"Wynik dodawania 5 + 7 to: {wynik}")


if __name__ == "__main__":
    main()
