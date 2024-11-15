def pattern4(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print()

if __name__ == "__main__":
    inp = int(input())
    pattern4(inp)
