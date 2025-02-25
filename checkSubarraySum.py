# 523. continuous subarray sum

def checkSubarraySum(nums, k):
    if len(nums) < 2:
        return False
    if k == 0:
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        return False
    if k < 0:
        k = -k
    sum = 0
    sumDict = {0:-1}
    for i in range(len(nums)):
        sum += nums[i]
        if sum % k in sumDict:
            if i - sumDict[sum%k] > 1:
                return True
        else:
            sumDict[sum%k] = i
    return False

def checkSubarraySum(nums, k):
    n = nums.size()
    if n < 2:
        return False
    mp = {}
    remainder = 0
    
    for i in range(n):
        remainder = (remainder + nums[i]) % k
        if remainder in mp:
            prevIndex = mp[remainder]
            if i - prevIndex >= 2:
                return True
        else:
            mp[remainder] = i
            
    return False