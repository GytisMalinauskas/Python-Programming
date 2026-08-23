from circular_buffer import CircularBuffer

def main():
    circular_buffer = CircularBuffer(2)
    circular_buffer.write(1)
    circular_buffer.write(2)
    circular_buffer.write(3)
    print(circular_buffer.read())
    circular_buffer.write(4)
    circular_buffer.overwrite(5)
    print(circular_buffer.read())
    print(circular_buffer.read())
    print(circular_buffer.read())
    
if __name__ == "__main__":
    main()