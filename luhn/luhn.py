class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num.strip()) < 2:
            return False
