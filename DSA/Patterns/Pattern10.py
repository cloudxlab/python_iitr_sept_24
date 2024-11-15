def pattern10(num):
    for i in range(1,num+1):
        print("* "*i)
    for i in range(num-1,0,-1):
        print("* "*i)
if __name__ == "__main__":
    inp = int(input())
    pattern10(inp)
