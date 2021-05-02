# membuat fungsi pembagian tanpa menggunakan div atau '/'
# menghasilkan integer

def pembagian(a,b):
    hasil = -1
    while a >= 0:
        a = a - b
        hasil += 1
    print(hasil)

     
pembagian(9,3)