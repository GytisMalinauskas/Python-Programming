from luhn import Luhn 

def main():
    luhn = Luhn("098 3434")
    luhn.valid()
    
if __name__ == "__main__":
    main()