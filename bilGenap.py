"""
Buat deret bilangan genap (angka 1-100)
"""
def genap():
    for num in range(1,101):
        if (num % 2) == 0:
            print(num)

genap()