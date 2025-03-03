def removeElement(nums, val):
    slow = 0
    fast = 0
    n = len(nums)
    
    while fast < n:
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
            
        fast += 1
        
    return slow

nums = [0,1,2,2,3,0,4,2]
print(nums[:removeElement(nums, 2)])

nums = [3,2,2,3]
print(nums[:removeElement(nums, 3)])