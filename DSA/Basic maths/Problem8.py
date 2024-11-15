def sum_all_divisor(num):

    result = 0
    for i in range(1, num+1):
        sum = 0
        for j in range(1, i+1):
            if i%j == 0:
                sum +=j
        result +=sum

    return result
    
if __name__ == "__main__":
    num = int(input())
    print(sum_all_divisor(num))
