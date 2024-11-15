def pattern19(num):

    for i in range(num):
        space = "  " * (i * 2)
        star = "* " * (num - i)
        print(star + space + star)

    for j in range(num - 1, -1, -1):
        space = "  " * (j * 2)
        star = "* " * (num - j)
        print(star + space + star)
    
if __name__ == "__main__":
    inp = int(input())
    pattern19(inp)
