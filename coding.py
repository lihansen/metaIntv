# 1920. Build Array from Permutation
def buildArray(nums):
    return [nums[nums[i]] for i in range(len(nums))]

# # in place 
# nums[0] = 0 + 6 * (nums[0] % 6) = 0
# nums[1] = 2 + 6 * (nums[2] % 6) = 2 + 6 * 1 = 8 // keeps the original value
# nums[2] = 1 + 6 * (nums[1] % 6) = 1 + 6 * 2 = 13 // adds the nums[i] value
# nums[3] = 5 + 6 * (nums[5] % 6) = 5 + 6 * 4 = 29
# nums[4] = 3 + 6 * (nums[3] % 6) = 3 + 6 * 5 = 33
# nums[5] = 4 + 6 * (nums[4] % 6) = 4 + 6 * 3 = 22
def buildArray2(nums):
    n = len(nums)
    for i in range(n):
        nums[i] = nums[i] + n * (nums[nums[i]] % n) # every number less than the n 
                                                    # because of it is permutation
                                                    # n * (nums[nums[i]] % n) represents how many ns in this position,
                                                    # which will not affect the original value
    for i in range(n):
        nums[i] //= n
    
    return nums




# 13. Roman to Integer

def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i, c in enumerate(s):
        if i < len(s) - 1 and d[c] < d[s[i+1]]:
            res -= d[c]
        else:
            res += d[c]

    return res



# 15. 3Sum

# [-4,-1,-1,0,1,2]
# fixed the first pointer, two pointers for the second and the third 
def threeSum2(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l, r = i+ 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
            while l<r and nums[l] == nums[l + 1]:
                l += 1
            while l<r and nums[r] == nums[r-1]:
                r -= 1

            l+=1
            r-=1
    return res
                           
def threeSum(nums):
    n = len(nums)
    res = []
    nums.sort()
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        r = n - 1
        for l in range(i+1, n-1):
            if l > i + 1 and nums[l-1] == nums[l]:
                continue
            
            while l < r and nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            
            if l < r and nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
    
    return res
            
            

if __name__ == '__main__':
    print('test')
    print(buildArray2([0,2,1,5,3,4])) # [0,1,2,4,5,3]
    print(romanToInt('III')) # 3
    print(threeSum([0,0,0,0])) # [[0,0,0]]
    print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(threeSum2([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(threeSum2([0,0,0,0])) # [[0,0,0]]