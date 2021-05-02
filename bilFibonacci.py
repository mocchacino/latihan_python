"""
Buat deret bilangan fibonacci (angka 1-100)
"""
def fibonacci():
    low = 1
    up = 100
    bil1 = low
    bil2 = 1
    total = 0
    while bil1 <= up:
        print(bil1)
        total = bil1 + bil2
        #change
        bil1 = bil2
        bil2 = total

fibonacci()