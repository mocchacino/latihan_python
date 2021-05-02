def isprime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

def range_prime(low, up):
    for num in range(low, up+1):
        if num > 1:
            for j in range(2, num):
                if(num % j) == 0:
                    break
            else:
                print(num)

def n_prime(ntimes):
    num = 2
    n = 1
    while n <= ntimes:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                n += 1
        num += 1
