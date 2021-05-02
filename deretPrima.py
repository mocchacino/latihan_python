"""
Buat deret bilangan prima (angka 1-100)
"""
def deretPrima():
    for num in range(1,101):
        for x in range(2,num):
            if (num % x) == 0:
                break
        else:
            print(num)

deretPrima()