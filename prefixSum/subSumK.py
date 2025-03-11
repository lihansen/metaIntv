def subarraySum(nums, k):
    sum = 0
    count = 0
    d = {0: 1}
    '''
    [1,2,3]
    d = dict()
    0:1 1:1 
    0:1 1:1 3:1 6:1
    '''
    for num, i in enumerate(nums):
        sum += num
        if sum - k in d:
            count += d[sum - k]

        d[sum] = d.get(sum, 0) + 1

    return count


print(subarraySum([1,2,3], 3))
