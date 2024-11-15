def count_dividing_digit(num):

    count = 0
    for digit in str(num):
        digit_int = int(digit)
        if digit_int  != 0 and num % digit_int == 0:
            count +=1
    
    return count
    
    
if __name__ == "__main__":
    inp = int(input())
    print(count_dividing_digit(inp))
