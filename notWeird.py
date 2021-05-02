"""
Weird diberikan N integer dari inputan(1-100), 
jika N bernilai ganjil, cetak “weird”, 
jika N bernilai genap dan diantara 2 dan 5,cetak “not Weird”, 
jika N bernilai genap dan diantara 6 dan 20, cetak “weird”, 
jika N bernilai genap dan N >20 , cetak “not weird”.
"""
def notWeird(num):
    if (num >= 1) and (num <= 100):
        if (num % 2) == 1:
            print("weird")
        elif (num % 2) == 0:
            if (num >= 2) and (num <= 5):
                print("not weird")
            elif (num >= 6) and (num <= 20):
                print("weird")
            elif (num > 20):
                print("not weird")

notWeird(21)