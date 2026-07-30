numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter element: "))

count = numbers.count(target)

print("Occurrences:", count)