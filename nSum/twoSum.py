def twoSum(nums, target):
    d = dict()
    
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        else:
            d[num] = i
            
            
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))