def merge_sort2(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return merge(left, right)


def merge2(left, right):
    res = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res


def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    mid = n // 2
    
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    res = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res
            
    



nums = [1,2,4,3,5]
print(merge_sort(nums))