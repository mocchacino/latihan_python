"""
Ilham beli sepatu seharga 165000 dengan diskon sebesar 15 persen, jika uang yang di bayar ilham sebesar 150000 , maka uang kembali sebesar
"""
def kembalian():
    harga = 165000
    diskon = 15
    dibayar =  150000

    return (dibayar - (harga - (harga * (1-diskon))))

print(kembalian())