from collections import Counter


def minWindow2(s, t):
    window = dict()
    need = dict(Counter(list(t)))

    left = 0
    right = 0
    valid = 0
    start = 0
    length = float("inf")

    while right < length:
        c = s[right]
        right += 1

        if c in need:
            window[c] = window.get(c, 0)

            if window.get(c, 0) == need.get(c, 0):
                valid += 1

        while valid == len(need):
            if right - left < length:
                start = left
                length = right - left

            d = s[left]

            left += 1

            if d in need:
                if window.get(d, 0) == need.get(d):
                    valid -= 1

                window[d] = window.get(d, 0) - 1

    return "" if length == float("inf") else s[start: start + length]


def minWindow3(s, t):
    if not s or not t:
        return ""

    map_t = Counter(t)
    required = len(t)

    left = 0
    right = 0
    min_start = 0
    min_len = float("inf")

    while right < len(s):
        char_r = s[right]
        if char_r in map_t:
            if map_t[char_r] > 0:
                required -= 1
            map_t[char_r] -= 1

        right += 1

        while required == 0:  # start to shrink the window
            if right - left < min_len:  # update window length
                min_len = right - left
                min_start = left

            char_l = s[left]
            if char_l in map_t:  # update the
                map_t[char_l] += 1
                if map_t[char_l] > 0:
                    required += 1

            left += 1

    return "" if min_len == float("inf") else s[min_start: min_start + min_len]


def minWindow4(s, t):
    if not s or not t:
        return ""

    left = 0
    right = 0

    min_start = 0
    min_len = float("inf")

    mapt = Counter(t)
    required = len(t)

    while right < len(s):
        c = s[right]
        if c in mapt:
            if mapt[c] > 0:
                required -= 1
            mapt[c] -= 1

        right += 1

        while required == 0:
            if min_len > right - left:
                min_len = right - left
                min_start = left

            c = s[left]
            if c in mapt:
                mapt[c] += 1
                if mapt[c] > 0:
                    required += 1

            left += 1

    return "" if min_len == float("inf") else s[min_start: min_start + min_len]


def minWindow5(s, t):
    need = Counter(t)
    window = dict()

    left = 0
    right = 0
    valid = 0
    start = 0
    length = float("inf")

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need):
            if right - left < length:
                start = left
                length = right - left

            c = s[left]
            if c in need:
                if window[c] == need[c]:
                    valid -= 1
                window[c] -= 1
            left += 1
    return "" if length == float("inf") else s[start: start + length]


def minWindow(s, t):
    if not s or not t:
        return ""

    map_t = Counter(t)
    required = len(t)  # how many num required

    left = 0
    right = 0
    min_len = float("inf")
    min_start = 0

    while right < len(s):
        char_right = s[right]
        if char_right in map_t:  # window has this char
            if map_t[char_right] > 0:
                required -= 1
            map_t[char_right] -= 1
        right += 1

        while required == 0:  # start shrink window
            if right - left < min_len:  # update min len
                min_len = right - left
                min_start = left

            char_left = s[left]
            if char_left in map_t:
                map_t[char_left] += 1
                if map_t[char_left] > 0:
                    required += 1

            left += 1

    return "" if min_len == float("inf") else s[min_start:min_start + min_len]


print(minWindow5(s="ADOBECODEBANC", t="ABC"))
print(minWindow5(s="a", t="aa"))
