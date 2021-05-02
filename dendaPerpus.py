"""
perpustakaan david meminjamkan beberapa jenis buku yaitu pelajaran,novel dan skripsi, 
buku-buku tersebut gratis dipinjam selama tidak melewati batas wktu pinjam 10 hari, 
jika melwati maka akan di kenakan denda perhari. 
untuk pelajaran perhari 2000, novel 5000 dan skripsi 10000, tentukan biaya denda nya ?
"""
def denda(buku, telat):
    bayar = 0
    if (buku == 'pelajaran'):
        bayar = 2000 * telat
    elif (buku == 'novel'):
        bayar = 5000 * telat
    elif (buku == 'skripsi'):
        bayar = 10000 * telat
    
    print(bayar)

denda('skripsi', 10)