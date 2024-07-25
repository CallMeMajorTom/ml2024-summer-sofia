N = int(input("Enter the count for numbers you would like to input: "))

numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

X = int(input("Enter the number value to search for: "))

found = False
for i, num in enumerate(numbers):
    if num == X:
        print(i + 1)  # Print the index (1-based)
        found = True
        break

if not found:
    print(-1)
