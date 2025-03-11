def searchRange(nums, target):
    n = len(nums)

    def searchLeftBound():
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                # if mid != n - 1 and nums[mid + 1] == target:
                #     return mid
                # else:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def searchRightBound():
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                if mid == n - 1 or nums[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                # if mid != 0 and nums[mid - 1] == target:
                #     return mid
                # else:
                right = mid - 1

            else:
                left = mid + 1
        return -1

    return [
        searchLeftBound(),
        searchRightBound()
    ]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
print(searchRange([], 0))  # [-1, -1]
print(searchRange([1], 1))  # [0, 0]
print(searchRange([2, 2], 2))  # [0, 1]
print(searchRange([1, 2, 2], 2))  # [1, 2]