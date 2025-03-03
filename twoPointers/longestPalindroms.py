def longestPalindrome1(s):
    n = len(s)

    def palindrome(s, left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

    res = ""

    for i in range(n):
        s1 = palindrome(s, i, i)
        s2 = palindrome(s, i, i + 1)

        if len(res) < len(s1):
            res = s1

        if len(res) < len(s2):
            res = s2

    return res


def longestPalindrome(s: str) -> str:
    n = len(s)
    res_left, res_right = 0, 0

    def palindrom(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return left, right

    for i in range(n):
        left1, right1 = palindrom(i, i)
        left2, right2 = palindrom(i, i+1)

        if res_right - res_left < right1 - left1:
            res_right = right1
            res_left = left1

        if res_right - res_left < right2 - left2:
            res_right = right2
            res_left = left2

    return s[res_left + 1: res_right]


print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))  # "bb"
print(longestPalindrome("a"))  # "a"
print(longestPalindrome("ac"))  # "a"
