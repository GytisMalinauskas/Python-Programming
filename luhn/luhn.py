class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        self.card_num
        if len(self.card_num.strip()) < 2:
            return False
        joined_card_num = "".join(self.card_num.split(" "))
        if not joined_card_num.isdecimal():
            return False
        
            
