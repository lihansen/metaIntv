def myAtoi(s):
    sign = 1
    result = 0
    index = 0
    n = len(s)
    
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    
    # remove spaces 
    while index < n and s[index] == " ":
        index += 1

    
    # sign
    if index < n and s[index] == "+":
        sign = 1 
        index  += 1
    
    elif index < n and s[index] == "-":
        sign = -1 
        index += 1
    
    while index < n and s[index].isdigit():
        digit = int(s[index])
        
        if (result > int_max // 10) or (
            result == int_max // 10 and digit > int_max % 10
        ):
            return int_max if sign == 1 else int_min
        
        result = 10 * result + digit
        index += 1
        
    return sign * result


print(myAtoi("42"))  # 42
print(myAtoi("   -42"))  # -42
print(myAtoi("4193 with words"))  # 4193
print(myAtoi("words and 987"))  # 0
print(myAtoi("-91283472332"))  # -2147483648
print(myAtoi("3.14159"))  # 3