"""
Seorang pengantar makanan akan melakukan perjalanan linear, menggunakan kendaraan 200cc. 
Diketahui jaraknya seperti berikut dan hitung berapa liter bensin yang dibutuhkan sampai perjalaan kembali ke toko?
Jarak:
toko ke tempat1=2Km
tempat1 ke tempat2 =500m
tempat2 ke tempat3 =1.5km
tempat3 ke tempat4 =2.5km
1 liter bensin untuk 2.5km
"""
def bensin():
    return (2 * (2 + 0.5 + 1.5 + 2.5)) / 2.5

print(bensin())