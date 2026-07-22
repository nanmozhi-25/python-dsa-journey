numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers:", even)
print("Odd Numbers:", odd)