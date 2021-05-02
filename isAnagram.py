def isAnagram(kalimat1, kalimat2):
    kalimat1.replace(" ", "")
    kalimat2.replace(" ", "")

    list_huruf1=[]
    list_huruf2=[]

    for huruf in kalimat1:
        if huruf != " ":
            list_huruf1.append(huruf)
    list_huruf1.sort()
    
    for huruf in kalimat2:
        if huruf != " ":
            list_huruf2.append(huruf)
    list_huruf2.sort()

    if list_huruf1 == list_huruf2:
        print("Anagram")
    else: print("Bukan Anagram")

isAnagram("Dormitory ","Dirty r    oom")