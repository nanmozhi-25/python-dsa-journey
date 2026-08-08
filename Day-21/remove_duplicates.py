nums = list(map(int, input("Enter sorted numbers: ").split()))

if nums:
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    print("Unique elements:", nums[:j])
else:
    print("Empty list")