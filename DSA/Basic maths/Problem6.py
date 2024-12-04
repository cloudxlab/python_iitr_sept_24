def armstrong_number(num):

    # counting digits
    dub_num = num
    count = 0
    while dub_num > 0:
        dub_num = dub_num//10
        count +=1

    # getting cube sum of number
    dub_num = num
    sum = 0
    while dub_num >0:
        rem = dub_num%10
        cube = 1

        # getting cube of digit
        for _ in range(count):
            cube *=rem

        sum +=cube
        dub_num //=10

    # Checking and returning
    if sum == num:
        return True
    else:
        return False
    
if __name__ == "__main__":
    num = int(input())
    print(armstrong_number(num))
