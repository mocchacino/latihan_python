# membuat counter berpaka kali angka tsb muncul dalam list

angka = [60, 90, 90, 25, 40, 35, 40]


def counterInList(list_angka):
    angka_unik = []
    count = 0
    for angka in list_angka:
        if angka not in angka_unik:
            angka_unik.append(angka)
    for unik in angka_unik:
        count = 0
        for angka in list_angka:
            if unik == angka:
                count += 1
        print("angka {} tampil {} kali".format(unik, count))

counterInList(angka)