
def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    max_length = 0
    window = dict()

    while right < len(s):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        right += 1

        while window.get(c) > 1:
            d = s[left]
            window[d] -= 1

            left += 1   

        if right - left > max_length:
            max_length = right - left
    
    return max_length

# def lengthOfLongestSubstring(s):
#     left = 0
    

print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring(""))  # 0