"""
Buat deret bilangan ganjil (angka 1-100)
"""
def ganjil():
    for num in range(1,101):
        if (num % 2) == 1:
            print(num)

ganjil()