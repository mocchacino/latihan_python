def firstNonRepeatingChar(kalimat):
    huruf_unik = []
    count = 0
    for huruf in kalimat:
        if huruf not in huruf_unik:
            huruf_unik.append(huruf)
    for unik in huruf_unik:
        count = 0
        for huruf in kalimat:
            if unik == huruf:
                count += 1
        if count > 1:
            continue
        else: 
            print(unik)
            break
                
firstNonRepeatingChar('tht')