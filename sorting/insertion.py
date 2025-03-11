def insertion_sort2(nums):
    n = len(nums)
    for i in range(1, n):
        candidate = nums[i]
        j = i - 1
        while j >= 0 and candidate < nums[j]:
            nums[j+1] = nums[j]
            j -= 1

        nums[j + 1] = candidate


def insertion_sort3(nums):
    n = len(nums)
    for i in range(1, n):
        candidate = nums[i]
        j = i - 1
        while j >= 0 and candidate < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = candidate


def insertion_sort4(nums):
    for i in range(1, len(nums)):
        candidate = nums[i]
        j = i - 1
        while j >= 0 and candidate < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = candidate
            
                
def insertion_sort5(nums):
    for i in range(1, len(nums)):
        candidate = nums[i]
        j = i - 1
        while j >=0 and candidate < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
            
        nums[j + 1] = candidate


def insertion_sort6(nums):
    n = len(nums)
    for i in range(1, n):
        candidate = nums[i]
        j = i - 1
        while j >= 0 and candidate < nums[j]:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = candidate


def insertion_sort(nums):
    for i in range(1, len(nums)):
        candidate = nums[i]
        j = i - 1
        while j >=0 and nums[j] > candidate:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = candidate
        
nums = [1, 4, 3, 5, 2]
insertion_sort(nums)
print(nums)
