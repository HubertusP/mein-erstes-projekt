def get_message() -> str:
    """
    Gibt die Nachricht der Anwendung zurück.
    So kann die Logik später leicht angepasst werden,
    ohne direkt in main() herumzuschreiben.
    """
    return "Feature Branch aktiv"


def show_message(message: str) -> None:
    """
    Gibt eine übergebene Nachricht auf der Konsole aus.
    """
    print(message)


def main() -> None:
    """
    Einstiegspunkt der Anwendung.
    Holt die Nachricht und zeigt sie an.
    """
    message = get_message()
    show_message(message)


if __name__ == "__main__":
    main()
    
