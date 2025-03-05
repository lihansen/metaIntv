from collections import Counter


def findAnagrams(s, p):
    left = 0
    right = 0
    validchars = 0

    need = Counter(p)
    window = dict()
    res = []

    while right < len(s):
        c = s[right]
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                validchars += 1

        right += 1

        while right - left >= len(p):
            if validchars == len(need):
                res.append(left)

            c = s[left]
            if c in need:
                if window[c] == need[c]:
                    validchars -= 1

                window[c] -= 1

            left += 1

    return res


print(findAnagrams("cbaebabacd", "abc"))  # [0, 6]
print(findAnagrams("abab", "ab"))  # [0, 1, 2]
