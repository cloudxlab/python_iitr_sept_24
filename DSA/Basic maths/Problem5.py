def LCM_GCF(a, b):

    result = []

    larger = max(a, b)
    lcm = larger
    while lcm%a != 0 or lcm%b != 0:
        lcm += larger
    result.append(lcm)

    for i in range(min(a,b), 0, -1):
        if a%i == 0 and b%i == 0:
            result.append(i)
            break
    
    return result
    
    
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(LCM_GCF(a,b))
