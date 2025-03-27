from pesel_validator import PeselValidator

def main():
    pesel = input("Podaj numer PESEL: ").strip()
    if PeselValidator.is_valid(pesel):
        print("PESEL jest poprawny.")
        print("Płeć:", "Mężczyzna" if PeselValidator.get_gender(pesel) == "M" else "Kobieta")
    else:
        print("PESEL jest niepoprawny.")

if __name__ == "__main__":
    main()
