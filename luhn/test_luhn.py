from luhn import Luhn 

def main():
    print(Luhn("098$ 3434").valid())
    print(Luhn("098 3434").valid())
    print(Luhn("9").valid())
    
if __name__ == "__main__":
    main()