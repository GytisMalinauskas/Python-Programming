from clock import Clock

def main():
    clock = Clock(10, 37)
    clock2 = Clock(34, 37)
    print(clock==clock2)
    
if __name__ == "__main__":
    main()