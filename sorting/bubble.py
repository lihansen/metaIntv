def bbSort(nums):
    n = len(nums)
    [1, 5, 2, 3, 4]
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]


nums = [1, 2, 4, 3, 5]
bbSort(nums)
print(nums)
