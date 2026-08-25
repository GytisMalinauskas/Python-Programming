class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num.strip()) < 2:
            return False
        joined_card_num = "".join(self.card_num.split(" "))
        if not joined_card_num.isdecimal():
            return False
        check_digit = joined_card_num[-1]
        reversed = joined_card_num[len(joined_card_num)-2::-1]
        index = 0
        sum = 0
        for character in reversed:
            if index % 2 == 0:
                odd = int(character) * 2
                if odd > 9:
                    odd -= 9
                sum += odd
            else:
                sum += int(character)
            index += 1
        modulus = (10 - (sum % 10)) % 10
        if modulus == check_digit:
            return True
        return False