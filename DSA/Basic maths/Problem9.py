def check_prime(num):

    if num == 1:
        return False

    if num == 2:
        return True
    
    for i in range(1, num):
        rem = num%i
        if rem == 0:
            return False
    
    return True
        
    
if __name__ == "__main__":
    num = int(input())
    print(check_prime(num))
