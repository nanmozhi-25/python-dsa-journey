numbers = list(map(int, input("Enter numbers: ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum element:", maximum)