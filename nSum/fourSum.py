def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []

    for first in range(n-3):
        if first > 0 and nums[first] == nums[first - 1]:
            continue

        for second in range(first + 1, n - 2):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue

            four = n - 1
            for third in range(second + 1, n-1):
                if third > second + 1 and nums[third-1] == nums[third]:
                    continue

                while third < four and nums[first] + nums[second] + nums[third] + nums[four] > target:
                    four -= 1

                if third != four and nums[first] + nums[second] + nums[third] + nums[four] == target:
                    res.append([nums[first], nums[second],
                               nums[third], nums[four]])

    return res


print(fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
print(fourSum([0, 0, 0, 0], 0))  # [[0,0,0,0]]
print(fourSum([-1, 0, 1, 2, -1, -4], -1))  # [[-4,0,1,2],[-1,-1,0,1]]
