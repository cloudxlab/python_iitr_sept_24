def pattern3(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    inp = int(input())
    pattern3(inp)
