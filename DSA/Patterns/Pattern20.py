def pattern20(num):

    for i in range(1,num+1):
        star = "* " * i
        space = "  " * ((num-i)*2)
        print(star + space + star)

    for j in range(num-1, 0, -1):
        star = "* "*j
        space = "  " * ((num-j)*2)
        print(star + space + star)
    
if __name__ == "__main__":
    inp = int(input())
    pattern20(inp)
