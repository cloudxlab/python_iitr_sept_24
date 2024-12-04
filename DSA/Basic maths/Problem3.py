def reverse_number(num):

    # Version 1: using maths not handling negative numbers

    # reverse = 0
    # while num >0:
    #     rem = num%10
    #     reverse = reverse*10 + rem
    #     num //=10
    
    # return reverse

    # Version 2: using string not handling negative numbers

    # num = str(num)
    # return num[::-1]

    # Version 3: Using maths also handle negative numbers
    is_neg = False
    reverse = 0
    
    if num< 0:
        is_neg = True
        num = num * -1

    while num >0:
        rem = num%10
        reverse = reverse*10 + rem
        num //=10
    
    if is_neg:
        return reverse*-1
    else:
        return reverse
    
    
if __name__ == "__main__":
    inp = int(input())
    print(reverse_number(inp))
