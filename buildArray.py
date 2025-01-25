# 1920. build array from permutation

def buildArray(nums):
    res = []
    
    for i in range(len(nums)):
        res.append(nums[nums[i]])
        
    return res

def buildArray2(nums):
    return [nums[nums[i]] for i in range(len(nums))]


# low + high
# hight =  
# nums[i] + (nums[nums[i]] % n) * n
def buildArray3(nums):
    n = len(nums)
    for i in range(n):
        org_val = nums[i] # keep the value as a remainder 
        new_val = nums[org_val]
        nums[i] = org_val + (new_val % n) * n
        
    for i in range(n):
        nums[i] //= n # get rid of the origin value 
    return nums



if __name__ == "__main__":
    print(buildArray([0,2,1,5,3,4])) # [0,1,2,4,5,3]
    print(buildArray2([0,2,1,5,3,4])) # [0,1,2,4,5,3]
    print(buildArray3([0,2,1,5,3,4])) # [0,1,2,4,5,3]
