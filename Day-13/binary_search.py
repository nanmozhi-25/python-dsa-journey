numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Element found at index", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Element not found")