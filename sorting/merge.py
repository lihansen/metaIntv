def merge(nums1, m, nums2, n):
    N = m + n
    p = N - 1
    p1 = m - 1
    p2 = n - 1
    
    while p1>= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
    
    while p1 >= 0:
        nums1[p] = nums1[p1]
        p -= 1
        p1 -= 1
        
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  # [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # [1]