"""
Tampilkan 5 angka random dari 1-100 :
– jika hasilnya <= 60 maka tampilkan tulisan “Kurang” disebelah angka tersebut
– jika >60 dan <= 70 maka tampilkan tulisan “Cukup” disebelah angka tersebut
– jika >70 dan <= 80 maka tampilkan tulisan “Baik” disebelah angka tersebut
– jika >80 maka tampilkan tulisan “Luar Biasa” disebelah angka tersebut
– angka yang tampil adalah kelipatan 5
"""
import random

def rateAngka():
    for i in range(0,5):
        angka = 1
        while angka % 5 != 0:
            angka = random.randint(1,100)
        if (angka <= 60):
            print("{} Kurang".format(angka))
        elif (angka <= 70):
            print("{} Cukup".format(angka))
        elif (angka <= 80):
            print("{} Baik".format(angka))
        elif (angka > 80):
            print("{} Luar Biasa".format(angka))
rateAngka()