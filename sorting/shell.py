def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
        

nums = [1,3,4,2,5]
shell_sort(nums)
print(nums)