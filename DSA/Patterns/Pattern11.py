def pattern11(num):
    for i in range(1, num+1):
        if i%2 == 0:
            pr = 0
        else: 
            pr = 1
        for j in range(i):
            print(pr, end="")
            pr = 1 - pr
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern11(inp)
