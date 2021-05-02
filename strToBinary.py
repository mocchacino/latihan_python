def strToBinary(kalimat):
    print("Kalimat: {}".format(kalimat))
    # using join() + bytearray() + format()
    # Converting String to binary
    biner = ''.join(format(i, '08b') for i in bytearray(kalimat, encoding ='utf-8'))

    print("Biner: " + biner)

strToBinary("PADA _ARA AFA RUDCARFAA BERUDAFG TA_UF DAF EEFGADACAF ACARA BERASAEA DA EADD CAPUTRA.WACTU ACARA BERDAFGSUFG EUDAA DARA SAAFG _ARA BAE SEBEDAS SAEPAA BAE 3 SGRE.VAFAA, PAVAER, FRAFSASCA DAF GDGA BUGA ACUT DAUFDAFG CE ACARA UDAFG TA_UFFQA.TGTAD QUAFTATQ PESERTA EEFCAPAA SERATUS GRAFG.")