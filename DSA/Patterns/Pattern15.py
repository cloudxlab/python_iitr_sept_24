def pattern15(num):
    
    for i in range(num, -1, -1):
        count = 0
        for j in range(i):
            print(chr(65 + count), end="")
            count +=1
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern15(inp)
