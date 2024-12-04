def plaindrome_number(num):

    # Using reverse maths
    dub_num = num
    reverse = 0
    while dub_num >0:
        rem = dub_num%10
        reverse = reverse*10 + rem
        dub_num //=10
    
    if reverse == num:
        return True
    else:
        return False

    # using string
    # num = str(num)
    # if (num == num[::-1]):
    #     return True
    # else:
    #     return False
    
    
if __name__ == "__main__":
    inp = int(input())
    print(plaindrome_number(inp))
