nums = list(map(int, input("Enter numbers: ").split()))

n = len(nums)
expected = n * (n + 1) // 2
actual = sum(nums)

print("Missing number:", expected - actual)