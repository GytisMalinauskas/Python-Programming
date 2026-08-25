"""A module for Luhn algorithm"""

class Luhn:
    """Initializes Luhn algoritm"""
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """Validates credit card number from accidental typing errors"""
        if len(self.card_num.strip()) < 2:
            return False
        joined_card_num = "".join(self.card_num.split(" "))
        if not joined_card_num.isdecimal():
            return False
        check_digit = int(joined_card_num[-1])
        reversed_card_number = joined_card_num[len(joined_card_num)-2::-1]
        index = 0
        sum_of_digits = 0
        for character in reversed_card_number:
            if index % 2 == 0:
                odd = int(character) * 2
                if odd > 9:
                    odd -= 9
                sum_of_digits += odd
            else:
                sum_of_digits += int(character)
            index += 1
        modulus = (10 - (sum_of_digits % 10)) % 10
        if modulus == check_digit:
            return True
        return False