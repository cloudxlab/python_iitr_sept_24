def numb_digit(num):

    # count digits using divide method
    count = 0
    while num > 0:
        num = num//10
        count +=1

    # count digit using log10 methed

    # import math
    # count = int(math.log10(num)+1)
    
    print(count)

    
    
if __name__ == "__main__":
    inp = int(input())
    numb_digit(inp)
