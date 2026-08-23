from circular_buffer import CircularBuffer

def main():
    circular_buffer = CircularBuffer(2)
    print(circular_buffer.read())

if __name__ == "__main__":
    main()