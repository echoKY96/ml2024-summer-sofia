from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    # Get N
    n = int(input("Enter a positive integer N: "))
    processor.initialize_data(n)
    
    # Get N numbers one by one
    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        processor.insert_data(i, number)
    
    # Get input X
    x = int(input("Enter the integer X to search: "))
    
    # Print search result
    result = processor.search_data(x)
    print(result)

if __name__ == "__main__":
    main()
