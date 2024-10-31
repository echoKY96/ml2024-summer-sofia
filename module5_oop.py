class NumberProcessor:
    def __init__(self):
        self.numbers = []
    
    def initialize_data(self, n):
        self.numbers = [None] * n
    
    def insert_data(self, index, number):
        self.numbers[index] = number


    def search_data(self, x):
        """Search for X in the list.

        Returns its 1-based index if found, else return -1.
        """
        if x in self.numbers:
            # Convert 0-based index to 1-based index.
            return self.numbers.index(x) + 1
        else:
            return -1

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
