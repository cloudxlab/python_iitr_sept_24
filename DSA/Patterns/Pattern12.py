def pattern12(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end="")
        for k in range((num-i)*2):
            print(" ",end="")
        for l in range(i,0,-1):
            print(l, end="")
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern12(inp)
