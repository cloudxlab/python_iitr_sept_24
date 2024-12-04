def pattern22(num):

    for i in range(num+(num-1)):
        for j in range(num+(num-1)):
            n = num - min(i, j, (num+(num-2)) - i, (num + (num-2)) - j)
            print(n, end="")
        print()
    
    
if __name__ == "__main__":
    inp = int(input())
    pattern22(inp)
