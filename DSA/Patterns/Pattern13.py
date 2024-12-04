def pattern13(num):
    count = 1
    for i in range(1, num+1):
        for j in range(i):
            print(str(count)+" ", end="")
            count +=1
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern13(inp)
