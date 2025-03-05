from collections import Counter


def checkInclusion2(s1, s2):
    s = s2
    t = s1

    need = Counter(t)
    window = dict()

    left = 0
    right = 0
    valid = 0

    while right < len(s):
        c = s[right]
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        right += 1

        while right - left >= len(t):
            if len(need) == valid:
                return True
            c = s[left]
            if c in need:
                if window[c] == need[c]:
                    valid -= 1
                window[c] -= 1

            left += 1

    return False


def checkInclusion(s1, s2):
    s = s2
    t = s1

    left = 0
    right = 0

    valid_chars = 0
    window = dict()  # count appr char in window
    need = Counter(t)  # this will never change

    while right < len(s):
        c = s[right]
        if c in need:
            window[c] = window.get(c, 0) + 1  # update this char statistic
            if window[c] == need[c]:
                valid_chars += 1

        right += 1

        while right - left >= len(t):
            if valid_chars == len(need):
                return True

            c = s[left]
            if c in need:
                if window[c] == need[c]:  # required char removed
                    valid_chars -= 1
                window[c] -= 1  # update char appr in window

            left += 1

    return False


print(checkInclusion("ab", "eidbaooo"))  # True
print(checkInclusion("ab", "eidboaoo"))  # False
