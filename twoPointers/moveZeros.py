def moveZeros(nums):
    n = len(nums)
    slow = 0

    for fast in range(n):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    for i in range(slow, n):
        nums[i] = 0

    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeros(nums))  # [1,3,12,0,0]
nums = [0]
print(moveZeros(nums))  # [0]
nums = [1]
print(moveZeros(nums))  # [1]
