from clock import Clock

def main():
    clock = Clock(35, 30)
    print(str(clock))
    print(repr(clock))
    print(str(clock + 20))
    print(repr(clock + 20))
    print(str(clock - 20))
    print(repr(clock - 20))
    clock2 = Clock(35, 30)
    clock3 = Clock(11, 40)
    print(clock==clock2)
    print(clock==clock3)        
    
if __name__ == "__main__":
    main()