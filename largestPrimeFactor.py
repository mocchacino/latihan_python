def largestPrimeFactor(num):
    temp = num
    for i in range(2, num):
        if temp % i == 0:
            temp /= i
            i-= 1
            return temp

print(largestPrimeFactor(15))