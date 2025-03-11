def search(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return target
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

print(search([-1,0,3,5,9,12], 9))  # 9
print(search([-1,0,3,5,9,12], 2))  # -1
print(search([5], 5))  # 5
print(search([5], 2))  # -1