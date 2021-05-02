"""
Disini dikasih sebuah soal tentang angka dan perulangan,
Waktu itu saya pilih kerjainnya di kertas, hehe (biar greget). 
Dikasih waktu 15 menit pengerjaannya.

Soalnya :

1) Ada sebuah angka seperti ini :
1.225.441

Berikan outputnya berupa :
1000000
200000
20000
5000
400
40
1
"""

def nilaiBesaran(nilai):
    #while nilai >= 0:
        juta = nilai/1000000
        juta = int(juta)*1000000
        print(juta)
        nilai = nilai - juta

        ratusribu = nilai / 100000
        ratusribu=int(ratusribu)*100000
        print(ratusribu)
        nilai = nilai - ratusribu

        puluhribu = nilai / 10000
        puluhribu=int(puluhribu)*10000
        print(puluhribu)
        nilai = nilai - puluhribu

        ribu = nilai / 1000
        ribu=int(ribu)*1000
        print(ribu)
        nilai = nilai - ribu

        ratus = nilai / 100
        ratus=int(ratus)*100
        print(ratus)
        nilai = nilai - ratus

        puluh = nilai / 10
        puluh=int(puluh)*10
        print(puluh)
        nilai = nilai - puluh

        print(nilai)


nilaiBesaran(1225441)
