from circular_buffer import CircularBuffer

def main():
    circular_buffer = CircularBuffer(2)
    circular_buffer.write(1)
    circular_buffer.overwrite(2)
    
if __name__ == "__main__":
    main()