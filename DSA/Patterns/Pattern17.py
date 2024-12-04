def pattern17(num):

    for i in range(1,num+1):
        count = 0
        for j in range((num-i)*2):
            print(" ",end="")

        for k in range(2*i-1):
            break_point = (2*i-1)//2
            print(chr(65 + count)+" ", end="")
            if (k < break_point):
                count +=1
            else:
                count -=1
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern17(inp)
