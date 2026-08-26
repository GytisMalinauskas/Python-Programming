from clock import Clock

def main():
    clock = Clock(11, 30)
    print(str(clock))
    print(repr(clock))
    print(str(clock + 20))
    print(repr(clock + 20))
    print(str(clock - 20))
    print(repr(clock - 20))            
    
if __name__ == "__main__":
    main()