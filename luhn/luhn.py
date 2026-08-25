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
        reversed = joined_card_num[slice(len(joined_card_num)-1, None, -1)]
        
        return (check_digit, reversed)