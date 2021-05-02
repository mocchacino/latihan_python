def CountCharacters(kalimat, cariHuruf):
    counter=0
    for huruf in kalimat:
        if huruf == cariHuruf:
            counter += 1
    print("Jumlah huruf yang muncul: {}".format(counter))

CountCharacters('Today is Monday', 'a')