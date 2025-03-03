def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    min_abs = float("inf")
    res = 0
    
    # -1 1 2 4 ,,,  target = 1
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        
        third = n - 1
        second = first + 1
        
        if second > first + 1 and nums[second] == nums[second - 1]:
            continue
        
        while second < third:
            total = nums[first] + nums[second] + nums[third]
            if abs(total - target) < min_abs:
                min_abs = abs(total - target)
                res = total 
                
            if total >= target:
                third -= 1 
            else:
                second += 1
            
    return res

print(threeSumClosest([-1,2,1,-4], 1)) # 2           
print(threeSumClosest([1,1,1,0], -100)) # 2
print(threeSumClosest([0,2,1,-3], 1)) # 0
print(threeSumClosest([1,2,4,8,16,32,64,128], 82)) # 82            