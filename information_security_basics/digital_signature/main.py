
def main():
    with open("sertifikatas.txt", "rb") as f:
        name, n, e = f.read()
        print(name, n, e)

if __name__ == "__main__":
    main()