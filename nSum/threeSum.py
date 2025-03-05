def threeSum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for first in range(n-2):
        if first > 0 and nums[first - 1] == nums[first]:
            continue
        
        third = n - 1
        for second in range(first + 1, n -1):
            if second > first + 1 and nums[second] == nums[second-1]:
                continue
            
            while third > second and nums[first] + nums[second] + nums[third] > 0: # when total is lt 0, `second` value need ot be larger
                third -= 1
                
            if second != third and nums[first] + nums[second] + nums[third] == 0:
                res.append([nums[first], nums[second], nums[third]])
    
    return res 


def threeSum2(nums):
    n = len(nums)
    res = []
    nums.sort()
    
    for first in range(n - 2):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        third = n - 1
        for second in range(first + 1, n-1):
            if second > first + 1 and nums[second-1] == nums[second]:
                continue
            while third > second and nums[first] + nums[second]+ nums[third] > 0:
                third -= 1
            if third > second and nums[first] + nums[second] + nums[third] == 0:
                res.append([nums[first], nums[second], nums[third]])
                
    return res

    
    
    
def threeSum3(nums):
    res = []
    n = len(nums)
    nums.sort()
    
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        
        third = n - 1
        for second in range(first + 1, n -1):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            
            while second < third and nums[first] + nums[second] + nums[third] > 0:
                third -= 1
                
            if second != third and nums[first] + nums[second] + nums[third] == 0:
                res.append([nums[first], nums[second], nums[third]])
                
    
    return res


def threeSum4(nums):
    nums.sort()
    n = len(nums)
    res = []
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        
        third = n - 1
        for second in range(first + 1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            
            while second < third and nums[first] + nums[second] + nums[third] > 0:
                third -= 1
                
            if second != third and nums[first] + nums[second] + nums[third] == 0:
                res.append([nums[first], nums[second], nums[third]])
            
    
    return res
    

def threeSum5(nums):
    nums.sort()
    n = len(nums)
    res = []
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
            
        second = first + 1
        third = n - 1
        while second < third:
            if second > first + 1 and nums[second] == nums[second - 1]:
                second += 1
                continue
            if third < n - 1 and nums[third] == nums[third + 1]:
                thrid -= 1
                continue
            
            total = nums[first] + nums[second] + nums[third]
            if total > 0: 
                third -= 1
            elif total == 0:
                res.append([nums[first], nums[second], nums[third]])
                third -= 1
                second += 1
            else:
                second += 1
    
    return res

print(threeSum5([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(threeSum5([])) # []
print(threeSum5([0])) # []
print(threeSum5([0,0,0])) # [[0,0,0]]
print(threeSum5([0,0,0,0])) # [[0,0,0]]
print(threeSum5([0,0,0,0,0])) # [[0,0,0]]
