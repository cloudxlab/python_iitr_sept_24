def pattern16(num):
    count = 0
    for i in range(1, num+1):
        for j in range(i):
            print(chr(65 + count), end="")
        count +=1
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern16(inp)
