def pattern18(num):

    for i in range(num):
        start_char = 65 + num-1
        for j in range(i + 1):
            print(chr(start_char - j), end=" ")
        print()
    
if __name__ == "__main__":
    inp = int(input())
    pattern18(inp)
