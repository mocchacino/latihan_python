"""
Belanja Hafid akan pergi belanja, 
belanja hafid dia tentukan dari berapa dia bawa uang, 
dengan uang diatas 750000 hafid mendapat “jas,
diatas 350000 hafid mendapat “celana panjang, 
diatas 225000 dapat “kemeja”, 
diatas 100000 dapat “kaos” 
dan diatas 50000 dapat “celana pendek” 
Contoh input: 
masukan jumlah uang : 220000 
output: hafid dapat kaos
"""
def belanja(uang):
    if (uang >= 750000):
        print("Hafid membeli jas")
    elif (uang >= 350000):
        print("Hafid membeli celana panjang")
    elif (uang >= 225000):
        print("Hafid membeli kemeja")
    elif (uang >= 100000):
        print("Hafid membeli kaos")
    elif (uang >= 50000):
        print("Hafid membeli celana pendek")

belanja(220000)