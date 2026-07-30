numbers = list(map(int, input("Enter numbers: ").split()))

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum element:", minimum)