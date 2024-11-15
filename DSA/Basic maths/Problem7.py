def all_divisor(num):

    result = []
    for i in range(1, num+1):
        if num%i == 0:
            result.append(i)
    
    return result
    
if __name__ == "__main__":
    num = int(input())
    print(all_divisor(num))
