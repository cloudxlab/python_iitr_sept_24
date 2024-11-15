def pattern6(num):
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    inp = int(input())
    pattern6(inp)
