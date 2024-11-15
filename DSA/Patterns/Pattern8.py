def pattern8(num):
    for i in range(num, 0, -1):
        stars = "* " * (2 * i - 1)
        print(" " * (num - i) * 2 + stars)

if __name__ == "__main__":
    inp = int(input())
    pattern8(inp)
