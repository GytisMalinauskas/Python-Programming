from luhn import Luhn 

def main():
    print(Luhn("098$ 3434").valid())
    
    
if __name__ == "__main__":
    main()