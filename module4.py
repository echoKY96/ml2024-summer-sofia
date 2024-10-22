N = int(input("Enter a positive integer N: "))

numbers = []

for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

X = int(input("Enter an integer X: "))

if X in numbers:
    # Output the 1-based index of X in the list
    print(numbers.index(X) + 1)
else:
    # Output -1 if X is not found
    print(-1)
