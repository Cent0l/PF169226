import re
from datetime import datetime

class PeselValidator:
    @staticmethod
    def validate_format(pesel):
        return bool(re.fullmatch(r'\d{11}', pesel))

    @staticmethod
    def validate_check_digit(pesel):
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        control_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
        check_digit = (10 - (control_sum % 10)) % 10
        return check_digit == int(pesel[10])

    @staticmethod
    def validate_birth_date(pesel):
        year = int(pesel[0:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])

        if 1 <= month <= 12:
            century = 1900
        elif 21 <= month <= 32:
            century = 2000
            month -= 20
        elif 41 <= month <= 52:
            century = 2100
            month -= 40
        elif 61 <= month <= 72:
            century = 2200
            month -= 60
        elif 81 <= month <= 92:
            century = 1800
            month -= 80
        else:
            return False

        year += century

        try:
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_gender(pesel)
        return "F" if int(pesel[9]) % 2 == 0 else "M"

    @staticmethod
    def is_valid(pesel):
        return (PeselValidator.validate_format(pesel)
                and PeselValidator.validate_check_digit(pesel)
                and PeselValidator.validate_birth_date(pesel))
