def removeDuplicates(nums):
    n = len(nums)
    
    slow = 1
    
    for fast in range(1, n):
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

nums = [1, 1, 2]
res = removeDuplicates(nums)
print(nums[:res]) # [1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
res = removeDuplicates(nums)
print(nums[:res]) # [0,1,2,3,4]
            